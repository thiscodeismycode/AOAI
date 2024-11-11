from ultralytics import YOLO

import argparse
import os

import time

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--test_dir", default="./data/test")
parser.add_argument("-o", "--out_dir", default="./result")

args = parser.parse_args()
test_path = args.test_dir
out_pat = args.out_dir

test_data = os.path.join(test_path, "test.jpeg")

def main():

    model = YOLO("./model/yolo11n.pt")

    print(f"Running inference on {test_data}")
    
    start = time.time()
    results = model(test_data)
    end = time.time()
    latency = end - start
    
    print(f'Total time taken: {latency:.2f}s')

    model.export(format="edgetpu")


if __name__=="__main__":
    main()
