import cv2
import numpy as np
import argparse
import os

def change_detection(image1, image2, threshold):

    img1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)
    diff = cv2.absdiff(img1, img2)
    _, binary_diff = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    return binary_diff


parser = argparse.ArgumentParser()
parser.add_argument("--predir", type=str, default='logs/chess1/renderonly_path_199999/', 
                        help='input data directory')
parser.add_argument("--postdir", type=str, default='logs/chess2/renderonly_path_199999/', 
                        help='input data directory')
parser.add_argument("--savedir", type=str, default='CD/chess/', 
                        help='save directory')
parser.add_argument("--threshold", type=int, default=80, 
                        help='threshold')
args = parser.parse_args()


image1_path = args.predir
image2_path = args.postdir
save_path = args.savedir
threshold_value = args.threshold
os.makedirs(save_path,exist_ok=True)

for i in range(0,120):
    i_str = str(i)
    i_str = i_str.zfill(3)
    img1= cv2.imread(image1_path+i_str+'.png')
    img2= cv2.imread(image2_path+i_str+'.png')

    result = change_detection(image1_path+i_str+'.png', image2_path+i_str+'.png', threshold_value)
    cv2.imwrite(save_path+i_str+'.png', result)


# for i in range(0, 120):
#     i_str = str(i)
#     i_str = i_str.zfill(3)
#     img1 = cv2.imread(image1_path+i_str+'.png')
#     cv2.imwrite(com_path+i_str+'-1'+'.png', img1)
#     img2 = cv2.imread(image2_path+i_str+'.png')
#     cv2.imwrite(com_path+i_str+'-3'+'.png', img2)
#     mask = cv2.imread(save_path+i_str+'.png')
#     cv2.imwrite(com_path+i_str+'-2'+'.png', mask)
