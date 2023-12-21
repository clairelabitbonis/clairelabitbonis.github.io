import argparse
from ultralytics import YOLO

def run(
    weights='yolov8n.pt',
    data="coco128.yaml",
    epochs=30,
    imgsz=640,
    name="exp",
    freeze=None,
    batch=8,
    device=0,
):
    
    model = YOLO(weights)
    model.train(data=data, epochs=epochs, imgsz=imgsz, name=name, device=device, batch=batch, freeze=freeze)



def parse_opt():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='coco128.yaml', help='data YAML')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--epochs', type=int, default=30, help='number of epochs')
    parser.add_argument('--name', type=str, default='', help='experiment name')
    parser.add_argument('--imgsz', type=int, default=640, help='image size')
    parser.add_argument('--freeze', type=int, default=None, help='freeze layers until n')
    parser.add_argument('--weights', type=str, default='yolov8s.pt', help='pre-trained weights')
    parser.add_argument('--batch', type=int, default=8, help='image batch')

    return parser.parse_args()

def main(opt):
    """Main function."""
    run(**vars(opt))


if __name__ == '__main__':
    opt = parse_opt()
    main(opt)