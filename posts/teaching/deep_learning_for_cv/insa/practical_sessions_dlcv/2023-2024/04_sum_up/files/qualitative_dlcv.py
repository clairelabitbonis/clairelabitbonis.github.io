import argparse
import glob
import os
from pathlib import Path
import cv2
from ultralytics import YOLO
import numpy as np

def create_unique_colors(n):

    colors = []

    while len(colors) < n:
        color = [(np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))]
        colors += color

    return colors

def run(
    weights='yolov8n.pt',
    source="video",
    path="path/to/video-or-folder",
    display_size=640
):
    ###########################################################
    #---------------------------------------------------------#
    #----------Loading the model with specific weights--------#
    #---------------------------------------------------------#
    ###########################################################

    print("Loading the network with " + weights)
    model = YOLO(weights)

    ###########################################################
    #---------------------------------------------------------#
    #--Reading the right input stream (images, video, webcam)-#
    #---------------------------------------------------------#
    ###########################################################

    if source == "video":
        print("Capturing " + path)
        video = cv2.VideoCapture(path)      ### Capture stream
        ret, frame = video.read()           ### Read the first frame

    elif source == "webcam":
        print("Capturing webcam")
        video = cv2.VideoCapture(0)         ### Capture stream
        ret, frame = video.read()           ### Read the first frame

    elif source == "folder":
        ret = False
        img_idx = 0

        ### List all .jpg in the folder
        filenames = sorted(glob.glob(os.path.join(path, "**/*.jpg"), recursive=True))
        print("Listing image files in " + path + "... " + str(len(filenames)) + " files")
        
        
        #### Read the first frame
        if len(filenames) > 0:
            frame = cv2.imread(filenames[img_idx]) 
            if frame is not None:
                ret = True
    
    elif source == "txt_file":
        ret = False
        img_idx = 0

        ### List all files listed in the txt_file
        with open(path, "r") as file:
            filenames = file.read().splitlines()
        
        print("Listing image files in " + path + ": " + str(len(filenames)) + " total")

        ### Supposedly, the txt file contains relative paths to images, and the file is 
        ### place inside this relative folder. We need to add the parent location to 
        ### read the full img path with OpenCV.
        ### /!\ If the .txt is placed elsewhere, surely it won't work... /!\
        file_path = Path(path)
        full_path = file_path.parent.absolute()
        
        if len(filenames) > 0:
            image_name = os.path.join(full_path, filenames[img_idx])
            frame = cv2.imread(image_name)
            if frame is not None:
                ret = True

    ###########################################################
    #---------------------------------------------------------#
    #---Creating the set of unique colors corresponding to----#
    #---each class of the dataset-----------------------------#
    #---------------------------------------------------------#
    ###########################################################

    colors = create_unique_colors(len(model.names))

    ###########################################################
    #---------------------------------------------------------#
    #---Looping over every image to process and display the---#
    #---bounding boxes, class and confidence score predicted--#
    #---by the model------------------------------------------#
    #---------------------------------------------------------#
    ###########################################################

    while ret:

        #### Resize image to desired display size
        h, w, c = frame.shape
        longest_border = np.amax(frame.shape[:2])
        ratio = display_size / longest_border
        frame = cv2.resize(frame, (int(ratio*w), int(ratio*h)))

        #### Infer YOLOv8 prediction on current frame
        results = model(frame)

        #### Process results list
        for result in results:

            #### Only process the object detection output (others are for classification, segmentation)
            #### See https://docs.ultralytics.com/reference/engine/results/#ultralytics.engine.results.Boxes 
            detections = result.boxes

            nb_detections = detections.shape[0]     ### Total number of detections for current frame
            boxes_xyxy = detections.xyxy            ### All x1, y1, x2, y2 boxes coordinates
            object_classes = detections.cls         ### All class identifiers (one for each box)
            confidence_scores = detections.conf     ### All confidence scores (one for each box)

            for i in range(nb_detections):
                
                ### Get detection infos one by one
                x1, y1, x2, y2 = boxes_xyxy[i].cpu().numpy().astype(int)
                obj_cls = int(object_classes[i])
                conf_score = confidence_scores[i]
                color = colors[obj_cls]

                ### Overlay the current detection in the current frame, with a rectangle for the box,
                ### another filled rectangle at the top of the box, and the label + score inside
                ### the filled rectangle.
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.rectangle(frame, (x1, y1), (x2, y1+30), color, -1)
                cv2.putText(frame, model.names[obj_cls] + ": " + str(float('%.2f' % conf_score)), (x1 + 2, y1 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)

        

        cv2.imshow("frame", frame)
        key = cv2.waitKey(0)
        if key == ord('q'): ### Stop if 'q' is pressed
            break

        ### Get the next frame
        if source == "video" or source == "webcam":
            ret, frame = video.read()
        elif source == "folder" or source == "txt_file":
            img_idx += 1
            
            if source == "folder":
                image_name = filenames[img_idx]
            elif source == "txt_file":
                image_name = os.path.join(full_path, filenames[img_idx])
            frame = cv2.imread(image_name)
            if frame is not None:
                ret = True

    if source == "video" or source == "webcam":
        video.release()
    cv2.destroyAllWindows()
    

def parse_opt():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='yolov8s.pt', help='path to the model weights')
    parser.add_argument('--source', type=str, default='video', help='input source, can be video, folder, txt_file or webcam')
    parser.add_argument('--path', type=str, default='', help='path to the video file or to the image folder, depending on the source param')
    parser.add_argument('--display_size', type=int, default=640, help='size of the displayed image')

    return parser.parse_args()

def main(opt):
    """Main function."""
    run(**vars(opt))


if __name__ == '__main__':
    opt = parse_opt()
    main(opt)


