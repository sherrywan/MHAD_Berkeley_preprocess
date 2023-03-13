'''
Author: wxy
Date: 2023-03-06 16:54:59
LastEditors: wxy
LastEditTime: 2023-03-08 15:26:59
Description: 
FilePath: /share/dataset/MHAD_Berkeley/stereo_camera/MHAD_Berkeley_preprocess/python/pgm2jpg.py
'''
from PIL import Image
import os
import cv2
import numpy as np

def save_img_p5(src_path, drc_path):
    img = Image.open(src_path)
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_BayerBG2BGR)
    cv2.imwrite(drc_path, img)
    
if __name__ == '__main__':
    for s in range(12):
        for a in range(11):
            for r in range(5):
                s = s+1
                a = a+1
                r = r+1
                print("--------start tranform pgm in s%d a%d r%d------------")
                corrs_fi = "../../Correspondences/corr_moc_img_s%02d_a%02d_r%02d.txt"%(s,a,r)
                src_folder = "../../../raw_data/Cluster01"
                drc_folder_0 = "../../Cluster01" 
                frames = np.loadtxt(corrs_fi)
                for frame in frames:
                    if frame[0]%3 != 0:
                        continue
                    else:
                        for c in range(4):
                            drc_folder = os.path.join(drc_folder_0 + "/Cam%02d"%(c+1), "S%02d"%s, "A%02d"%a, "R%02d"%r)
                            os.makedirs(drc_folder, exist_ok=True)
                            src_file = os.path.join(src_folder+"/Cam%02d"%(c+1), "S%02d"%s, "A%02d"%a, "R%02d"%r, "img_l01_c%02d_s%02d_a%02d_r%02d_%05d.pgm"%(c+1,s,a,r,frame[0]))
                            drc_file = os.path.join(drc_folder, "img_l01_c%02d_s%02d_a%02d_r%02d_%05d.jpg"%(c+1,s,a,r,frame[0]))
                            if os.path.exists(src_file):
                                save_img_p5(src_file, drc_file)
                            else:
                                print("Error: {} is missing!".format(src_file))
