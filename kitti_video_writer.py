import os
import cv2

# image path: /home/uav/Downloads/kitti_raw_data/2011_09_26_drive_0009_sync/2011_09_26/2011_09_26_drive_0009_sync/image_02/data
im_dir = '/home/uav/Downloads/kitti_raw_data/2011_09_26_drive_0009_sync/2011_09_26/2011_09_26_drive_0009_sync/image_02/data'
# output video path
video_dir = '/home/uav/Desktop/imageSequence2Video'
if not os.path.exists(video_dir):
    os.makedirs(video_dir)
# set saved fps
fps = 10
# get frames list
frames = sorted(os.listdir(im_dir))
# w,h of image
img = cv2.imread(os.path.join(im_dir, frames[0]))
img_size = (img.shape[1], img.shape[0])
# get seq name
seq_name = os.path.dirname(im_dir).split('/')[-1]
# splice video_dir
video_dir = os.path.join(video_dir, seq_name + '.mp4')
#fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
#fourcc = cv2.VideoWriter_fourcc('MP4V')
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# also can write like:fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# if want to write .mp4 file, use 'MP4V'
videowriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)

for frame in frames:
    f_path = os.path.join(im_dir, frame)
    image = cv2.imread(f_path)
    videowriter.write(image)
    print(frame + " has been written!")

videowriter.release()
