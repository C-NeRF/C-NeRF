import cv2
import imageio
import os, sys
import numpy as np
from PIL import Image
from torchvision.transforms import functional as f
from matplotlib import pyplot as plt
import open3d as o3d
import argparse



def display_inlier_outlier(cloud1, cloud2, threshold):
    dists = cloud1.compute_point_cloud_distance(cloud2)
    dists = np.asarray(dists)
    ind = np.where(dists<threshold)[0] 

    inlier_cloud = cloud1.select_by_index(ind)
    outlier_cloud = cloud1.select_by_index(ind, invert=True)

    outlier_cloud.paint_uniform_color([0, 0, 1])
    inlier_cloud.paint_uniform_color([1, 0, 0])

    return inlier_cloud
    

parser = argparse.ArgumentParser()
parser.add_argument("--name", type=str, default='chess', 
                        help='scene name')
args = parser.parse_args()

name = args.name


path = "PC/"+name+"/"
database0 = np.load("PC/"+name+"/000.npy")

pc0 = o3d.geometry.PointCloud()
pc0.points = o3d.utility.Vector3dVector(database0)

t = 0
for i in range(0, 120):

    i_str = str(i)
    i_str = i_str.zfill(3)
    database1 = np.load(path+i_str+".npy")

    pc1 = o3d.geometry.PointCloud()
    pc1.points = o3d.utility.Vector3dVector(database1)


    inline1 = display_inlier_outlier(pc1, pc0, 0.005)  
    inline2 = display_inlier_outlier(pc0, pc1, 0.005)  

    point1 = np.array(inline1.points)
    point2 = np.array(inline2.points)
    pcd = np.vstack([point1,point2])

    pc0.points = o3d.utility.Vector3dVector(pcd)
    # o3d.visualization.draw_geometries([pc0],
    #                                   window_name="重叠和非重叠点",
                                      
    #                                   mesh_show_back_face=False, width=1500, height=1500)
# o3d.visualization.draw_geometries([pc0],
#                                       window_name="重叠和非重叠点",
                                      
#                                       mesh_show_back_face=False, width=1500, height=1500)

A=np.asarray(pc0.points)

np.save("PC/denoising_"+name+".npy", A)