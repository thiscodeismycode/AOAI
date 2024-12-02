import os
import yaml
import tqdm
import argparse

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=str, default="/home/user/data/sea_safe_dataset/train/images")
    parser.add_argument('--input_label', type=str, default="/home/user/data/sea_safe_dataset/train/labels")
    parser.add_argument('--crop_dir', type=str, default="/home/user/data/sea_safe_dataset/cropped/images")
    parser.add_argument('--crop_label', type=str, default="/home/user/data/sea_safe_dataset/cropped/labels")
    parser.add_argument('--output_dir', type=str, default="/home/user/data/sea_safe_dataset/augmented/images")
    parser.add_argument('--output_label', type=str, default="/home/user/data/sea_safe_dataset/augmented/labels")


    args = parser.parse_args()
    input_dir = args.input_dir
    input_label = args.input_label
    crop_dir = args.crop_dir
    crop_label = args.crop_label
    output_dir = args.output_dir
    output_label = args.output_label

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    if not os.path.isdir(output_label):
        os.makedirs(output_label)

    # Get background image
    # Get background label
    # Get cropped image
    # Resize images so that they are of the same shapes
    # 합체
    # Create new label
    # Save them all into new directories



    print("Augmentation done")

    return

if __name__ == '__main__':
    main()
