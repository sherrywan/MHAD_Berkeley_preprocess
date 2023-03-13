clear;
clc;

src = 'D:/dataset/MHAD/raw_data';
drc = 'D:/dataset/MHAD/stereo_camera';
f1 = fopen(sprintf('%s/frames_r01.txt',drc), 'w')
f2 = fopen(sprintf('%s/frames_r02.txt',drc), 'w')
f3 = fopen(sprintf('%s/frames_r03.txt',drc), 'w')
f4 = fopen(sprintf('%s/frames_r04.txt',drc), 'w')
f5 = fopen(sprintf('%s/frames_r05.txt',drc), 'w')

for s=1:12
    for a=1:11
        for r=1:5
            im_mc_f = sprintf('%s/Camera/Correspondences/corr_moc_img_s%02d_a%02d_r%02d.txt',src,s,a,r);
            if exist(im_mc_f, 'file')==0
                fprintf('%s does not exist', im_mc_f);
                continue
            end
            
            im_mc = load(sprintf('%s/Camera/Correspondences/corr_moc_img_s%02d_a%02d_r%02d.txt',src,s,a,r));
            [skel,channel,framerate] = bvhReadFile(sprintf('%s/Mocap/SkeletalData/skl_s%02d_a%02d_r%02d.bvh',src,s,a,r));
            skel_jnt = 10*chan2xyz(skel,channel);
            
            if r==1
                fprintf(f1, '%d\t%d\t%d\n',s,a,size(im_mc,1));
            end
            if r==2
                fprintf(f2, '%d\t%d\t%d\n',s,a,size(im_mc,1));
            end
            if r==3
                fprintf(f3, '%d\t%d\t%d\n',s,a,size(im_mc,1));
            end
            if r==4
                fprintf(f4, '%d\t%d\t%d\n',s,a,size(im_mc,1));
            end
            if r==5
                fprintf(f5, '%d\t%d\t%d\n',s,a,size(im_mc,1));
            end
            
%             for i=1:size(im_mc,1)
%                  % get the skeleton frame
%                  jnt = reshape(skel_jnt(im_mc(i,3)+1,:),3,[]);
%                  fid = fopen(sprintf('%s/Skeleton/jnt_s%02d_a%02d_r%02d_%05d.txt',drc,s,a,r,im_mc(i,1)),'w');
%                  for j=1:size(jnt,2)
%                      fprintf(fid,'%4.4f\t%4.4f\t%4.4f\n',jnt(1,j),jnt(2,j),jnt(3,j));
%                  end
%                  fclose(fid);
%             end
        end
    end
end

fclose(f1)
fclose(f2)
fclose(f3)
fclose(f4)
fclose(f5)