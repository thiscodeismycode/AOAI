import os
import cv2
from tqdm import tqdm
import numpy as np
import argparse
from PIL import Image

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', type=str, default="/home/user/data/sea_safe_dataset/train/images")
    parser.add_argument('--input_label', type=str, default="/home/user/data/sea_safe_dataset/train/labels")
    parser.add_argument('--output_dir', type=str, default="/home/user/data/sea_safe_dataset/cropped/images")
    parser.add_argument('--output_label', type=str, default="/home/user/data/sea_safe_dataset/cropped/labels")

    args = parser.parse_args()
    input_dir = args.input_dir
    input_label = args.input_label
    output_dir = args.output_dir
    output_label = args.output_label

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    if not os.path.isdir(output_label):
        os.makedirs(output_label)

    # Get image file name
    # Open corresponding label file
    # Find label 1

    labels = [f for f in os.listdir(input_label) if os.path.isfile(os.path.join(input_label, f))]
    for label in tqdm(labels):
        name = label.split('.')[0]
        with open(os.path.join(input_label, label), 'r') as l:
            lines = l.readlines()
        masks = None
        img = None
        buoys = []
        for line in lines:
            _line = line.strip()
            _line = _line.split(' ')

            if _line[0] == '1':
                buoys.append(line)
                # Background -> 0 with binary mask: create a 0 matrix and find where to fill in with 1
                image_name = os.path.join(input_dir, f'{name}.jpg')
                img = cv2.imread(image_name)
                # print(f"Opened image {image_name}")
                # _img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                # img_rgb = _img_rgb.copy()
                # height, width, depth = img_rgb.shape
                height, width, depth = img.shape
                # print(f"img rgb shape: {img.shape}")
                mask = np.zeros_like(img)

                center_x = int(float(_line[1]) * width)
                center_y = int(float(_line[2]) * height)
                w = int(float(_line[3]) * width) // 2
                h = int(float(_line[4]) * height) // 2

                assert w > 0, "Width is zero"
                assert h > 0, "Height is zero"
                x_1 = center_x - w
                x_2 = center_x + w
                y_1 = center_y - h
                y_2 = center_y + h

                mask[y_1:y_2, x_1:x_2, :] = 1
                if masks is None:
                    masks = mask
                else:
                    masks += mask

        # _masked_image = img_rgb * mask
        if masks is not None:
            assert img is not None, "Image is None"
            masked_image = img * masks
            assert np.sum(masked_image) > 0, "Empty image"
            # masked_image = cv2.cvtColor(_masked_image, cv2.COLOR_RGB2BGR)

            # Save image file
            im = Image.fromarray(masked_image)
            im.save(os.path.join(output_dir, f'{name}_crop.jpg'))

            # Save label file
            with open(os.path.join(output_label, f'{name}_crop.txt'), 'w') as ll:
                for buoy in buoys:
                    ll.write(buoy)

    print("Cropping done")


if __name__ == '__main__':
    main()
