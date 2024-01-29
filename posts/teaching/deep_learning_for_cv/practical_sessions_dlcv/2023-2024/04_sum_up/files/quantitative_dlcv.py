import argparse
from ultralytics import YOLO

def run(
    weights='yolov8n.pt',
    data="coco128.yaml",
    batch=8,
    imgsz=640,
    device=0,
    split="val",
    plots=False
):
    
    model = YOLO(weights)
    metrics = model.val(data=data, device=device, batch=batch, split=split, plots=plots, imgsz=imgsz)


def parse_opt():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='coco128.yaml', help='data YAML')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--weights', type=str, default='yolov8s.pt', help='pre-trained weights')
    parser.add_argument('--batch', type=int, default=8, help='image batch')
    parser.add_argument('--imgsz', type=int, default=640, help='image size')
    parser.add_argument('--split', type=str, default="val", help='dataset split to use for validation (val, test or train)')
    parser.add_argument('--plots', action='store_true', help='save plots and images during validation')

    return parser.parse_args()

def main(opt):
    """Main function."""
    run(**vars(opt))


if __name__ == '__main__':
    opt = parse_opt()
    main(opt)