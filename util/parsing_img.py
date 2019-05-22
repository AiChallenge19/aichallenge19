import glog as log
import os

def main(base_dir):
    clip_list = os.listdir(base_dir)
    for clip in clip_list:
        img_list = os.listdir(os.path.join(base_dir,clip))
        for img in img_list:
            fname, ext = os.path.splitext(img)
            if ext == '.jpg':
                print(img)












if __name__ == "__main__":
    base_dir = "/home/dylee/Archive/data/ai_challenge/track_01/t1_video"
    main(base_dir)