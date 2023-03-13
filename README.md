<!--
 * @Author: sherrywaan sherrywaan@outlook.com
 * @Date: 2023-03-08 15:02:40
 * @LastEditors: sherrywaan sherrywaan@outlook.com
 * @LastEditTime: 2023-03-13 14:36:52
 * @FilePath: /dataset/MHAD_Berkeley/stereo_camera/MHAD_Berkeley_preprocess/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# MHAD_Berkeley_preprocess

## data prepare
1.download the data from Camera/Cluster01 Mocap Calibration in https://tele-immersion.citris-uc.org/berkeley_mhad  
2.download demo_image, unzip it

## data transformation
1.move two .m files from matlab folder to demo_image  
2.run skeleton_generation.m to transform from bvh to joint 3d location with shape (35,3)
3.run pgm2jpg.m to transform from pgm files to jpg files

## data checking
1. run python/check_dataset.py to check projection parameters, multiview data pair size  
if you want to check the projection parameters, please mkdir test/Cam_i and add corresponding imgaes to them
