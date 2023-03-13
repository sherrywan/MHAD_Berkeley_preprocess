'''
Author: wxy
Date: 2023-03-07 10:10:36
LastEditors: sherrywaan sherrywaan@outlook.com
LastEditTime: 2023-03-13 16:22:13
Description: 
FilePath: /share/dataset/MHAD_Berkeley/stereo_camera/MHAD_Berkeley_preprocess/python/check_dataset.py
'''

import os
import glob
import cv2
import numpy as np


def check_multiview_data(src, frame_e_f):
    src = os.path.join(src, 'Cluster01')
    
    # delete files end with %3!=0
    src_folder = []
    for s in range(12):
        for a in range(11):
            for r in range(5):
                for c in range(4):
                    fo = os.path.join(src, 'Cam%02d'%(c+1), 'S%02d'%(s+1), 'A%02d'%(a+1), 'R%02d'%(r+1))
                    src_folder.append(fo)
    imgs_list = []
    for src_f in src_folder:
        for f in os.listdir(src_f):
            f_num = int(f[-9:-4])
            if f_num%3 != 0 :
                os.remove(os.path.join(src_f, f))
    
    # data missing problem is fixed by MHAD team
    # # delete files whose same frame missed in other views
    # frames_err = []
    # with open(frame_e_f, 'r') as fi:
    #     for line in fi:
    #         line_list = line.split('\t')
    #         s = int(line_list[0])
    #         a = int(line_list[1])
    #         r = int(line_list[2])
    #         c = int(line_list[3])
    #         f = int(line_list[4])
    #         frames_err.append([s,a,r,c,f])
    
    # for frame_err in frames_err:
    #     for c in range(4):
    #         c =c +1          
    #         fi = os.path.join(src, 'Cam%02d'%(c), 'S%02d'%(frame_err[0]), 'A%02d'%(frame_err[1]), 'R%02d'%(frame_err[2]), 'img_l01_c%02d_s%02d_a%02d_r%02d_%05d.jpg'%(c,frame_err[0],frame_err[1],frame_err[2],frame_err[4]))
    #         if os.path.exists(fi):
    #             os.remove(fi)


def check_multiview_pair_datalen(src):
    src = os.path.join(src, 'Cluster01')
    # check the datalength of same actions between different views
    for s in range(12):
        for a in range(11):
            for r in range(5):
                file_nums = []
                for c in range(4):
                    fo = os.path.join(src, 'Cam%02d'%(c+1), 'S%02d'%(s+1), 'A%02d'%(a+1), 'R%02d'%(r+1))
                    fo_len = len(os.listdir(fo))
                    file_nums.append(fo_len)
                if len(set(file_nums))!=1:
                    print("Error: s{} a{} r{} multiview pair dataset size error with length {}!".format(s,a,r,file_nums))

         
def wrd2img(jnt3d, camera_idx):
    # wrd to cluster
    R_cluster1 = np.array([0.895701051, 0.002872461, -0.444647521, 0.050160084, -0.994248986, 0.094619878, -0.441818565, -0.107054681, -0.890693903]).reshape(3,3)
    t_cluster1 = np.array([-654.69244384, 1101.511840820, 3154.582519531]).reshape(3,1)
    
    # cluster to camera
    if camera_idx == 0:
        K = np.array([523.62481689, 0., 351.50247192, 0., 524.78002930, 225.29899597, 0., 0., 1.]).reshape(3,3)
        R = np.array([1,0,0,0,1,0,0,0,1]).reshape(3,3)
        t = np.array([0,0,0]).reshape(3,1)
    elif camera_idx == 1:
        K = np.array([532.78863525, 0., 320.36187744, 0., 533.49108887, 231.61149597, 0., 0., 1.]).reshape(3,3)
        R = np.array([0.9942,-0.0290,0.1034,0.0314,0.9993,-0.0222,-0.1027,0.0254,0.9944]).reshape(3,3)
        t = np.array([-113.2355,-3.1258,5.3590]).reshape(3,1)
    elif camera_idx == 2:
        K = np.array([535.76379395, 0., 351.78421021, 0., 536.48388672, 258.91003418, 0., 0., 1.]).reshape(3,3)
        R = np.array([0.9943,-0.0329,0.1012,0.0391,0.9974,-0.0599,-0.0990,0.0635,0.9931]).reshape(3,3)
        t = np.array([-225.5759,-8.3706,10.4491]).reshape(3,1)
    elif camera_idx == 3:
        K = np.array([541.68511963, 0., 334.84011841, 0., 542.19091797, 229.06407166, 0., 0., 1.]).reshape(3,3)
        R = np.array([0.9838,-0.0182,0.1781,0.0205,0.9997,-0.0110,-0.1778,0.0145,0.9840]).reshape(3,3)
        t = np.array([-331.1895,-5.8068,43.4163]).reshape(3,1)

    # wrd to camera
    z = np.array([0,0,0,1]).reshape(1,4)
    T_cluster1 = np.hstack((R_cluster1, t_cluster1))
    T_cluster1 = np.vstack((T_cluster1, z))
    T = np.hstack((R, t))
    T = np.vstack((T, z))
    T_fin = T@T_cluster1
    T_fin = T_fin[:3]
    
    # wrd to img
    P = K@T_fin
    
    # projection
    jnt3d_H = np.ones((jnt3d.shape[0],4))
    jnt3d_H[:,:3] = jnt3d
    jnt2d_H = (P@jnt3d_H[:,:,np.newaxis]).reshape(-1,3)
    jnt2d = jnt2d_H[:,:2] / jnt2d_H[:,2][:,np.newaxis]
    
    return jnt2d
    
    
if __name__=="__main__":
    src = '../../'
    print("---------Start checking multiview dataset frames---------")
    frame_error_file = os.path.join(src,'MHAD_Berkeley_preprocess/frames_err.txt')
    check_multiview_data(src, frame_error_file)
    
    print("---------Start checking multiview pair length---------")
    check_multiview_pair_datalen(src)
                
    print("---------Start checking projection---------")
    c = 2
    img_folder = "../test/cam_{}".format(c)
    imgs = os.listdir(img_folder)
    for img in imgs:
        if "joint" in img:
            continue
        # load 3d joints and project ro image plane
        s = int(img[13:15])
        a = int(img[17:19])
        r = int(img[21:23])
        f = int(img[-9:-4])
        jnt_fi = os.path.join(src, "Skeleton/jnt_s%02d_a%02d_r%02d_%05d.txt"%(s,a,r,f))
        jnt3d = np.loadtxt(jnt_fi)
        jnt2d = wrd2img(jnt3d, c)
        
        # draw joints and its idx
        pic = cv2.imread(os.path.join(img_folder,img))
        for jnt_idx, jnt in enumerate(jnt2d):
            cv2.circle(pic, (int(jnt[0]), int(jnt[1])), 4, (0,0,250), -1)
            cv2.putText(pic, str(jnt_idx), (int(jnt[0]), int(jnt[1])), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255),2)
        cv2.imwrite(os.path.join(img_folder, img[:-4]+"_joint.jpg"), pic)
        
            
        
    
    