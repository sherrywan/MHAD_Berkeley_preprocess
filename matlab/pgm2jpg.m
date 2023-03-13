clear;
clc;

src = 'D:/dataset/MHAD/raw_data';
drc = 'D:/dataset/MHAD/stereo_camera';


%for s=1:12
%   for a=1:11
%        for r=1:5
%           for c=1:4
%               drc_folder = sprintf('%s/Camera/Cluster01/Cam%02d/S%02d/A%02d/R%02d',drc,c,s,a,r);
%               mkdirs(drc_folder);
%           end
%       end
%   end
%end

f_e = fopen(sprintf('%s/frames_err.txt',drc), 'w');
for s=1:12
    for a=1:11
        for r=1:5
            im_mc_f = sprintf('%s/Camera/Correspondences/corr_moc_img_s%02d_a%02d_r%02d.txt',src,s,a,r);
            if exist(im_mc_f, 'file')==0
                fprintf('%s does not exist', im_mc_f);
                continue
            end
            im_mc = load(im_mc_f);
            for c=1:4
                for i=1:3:size(im_mc,1)
                    drc_folder = sprintf('%s/Camera/Cluster01/Cam%02d/S%02d/A%02d/R%02d',drc,c,s,a,r);
                    img_f = sprintf('%s/Camera/Cluster01/Cam%02d/S%02d/A%02d/R%02d/img_l01_c%02d_s%02d_a%02d_r%02d_%05d.pgm',src,c,s,a,r,c,s,a,r,im_mc(i,1));
                    if exist(img_f, 'file')==0
                        fprintf('%s does not exist!\n', img_f);
                        continue
                    end
                    [f,m] = fopen(img_f);
                    if length(fgets(f))~=3
                        fprintf('%s error!\n', img_f);
                        fprintf(f_e, '%d\t%d\t%d\t%d\t%d\n',s,a,r,c,im_mc(i,1));
                        fclose(f);
                        continue
                    end
                    fclose(f);
                    img = imread(img_f);
                    img = demosaic(img,'grbg');
                    imwrite(img, sprintf('%s/img_l01_c%02d_s%02d_a%02d_r%02d_%05d.jpg',drc_folder,c,s,a,r,im_mc(i,1)));
                    delete(img_f);
                end
            end
        end
        
    end
end
fclose(f_e);

function mkdirs(thepath)
    if ~exist(thepath, 'dir')
        [suppath, ~] = fileparts(thepath);
        if ~exist(suppath, 'dir')
            mkdirs(suppath)
        end
    end
    mkdir(thepath)
end