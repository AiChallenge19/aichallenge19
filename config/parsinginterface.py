"""
Copyright 2018 The 빈공지능. All Rights Reserved.
======================================
base scenario data parsing API
======================================
Author : Dongyul Lee
Issue date : 23, May, 2019
ver : 1.0.0

============팀
Descriptions
============
data parsing interface

============
depedencies
============
tensorflow=...
=====

"""


import argparse
import numpy as np
from config import globalconfig
import glog as log
# import cv2
import os
import glob

mode_list = {'TRAIN' : 'TRAIN', 'VALIDATION' : 'VALIDATION', 'TEST' : 'TEST'}

save_folder_list = {'vra' : 'vra', 'aa' : 'aa'}


class parsinginterface(globalconfig.globalconfig):
    def __init__(self):
        super(parsinginterface, self).__init__()
        self.parser = argparse.ArgumentParser(description='Data configuration and data parsing')
        # self.real = True
        # h = self._get_img_h()
        # w = self._get_img_w()


    def _get_img(self):
        self.parser.add_argument('--height', type=int, default=self._get_config_image_h())
        self.parser.add_argument('--width', type=int, default=self._get_config_image_w())
        self.parser.add_argument('--channel', type=int, default=self._get_config_image_c())

    def _get_gan_patch(self):
        self.parser.add_argument('--pix2pix_img_channels', type=int, default=self._get_img_channels())
        self.parser.add_argument('--pix2pix_gt_channels', type=int, default=self._get_gt_channels())
        self.parser.add_argument('--pix2pix_cls_channels', type=int, default=self._get_cls_channels())


        self.parser.add_argument('--pix2pix_patch_number', type=int, default=self._get_patch_number())
        self.parser.add_argument('--pix2pix_patch_height', type=int, default=self._get_patch_height())
        self.parser.add_argument('--pix2pix_patch_width', type=int, default=self._get_patch_width())

    #get train information
    def _get_gpu(self,mode):
        self.parser.add_argument('--gpu', type=str, default=self._get_config_gpu(mode))

    def _get_epoch(self,mode):
        self.parser.add_argument('--epoch', type=int, default=self._get_config_epoch(mode))

    def _get_lr(self,mode):
        self.parser.add_argument('--lr', type=float, default=self._get_config_train_lr(mode))

    def _get_tf_mem_frc(self,mode):
        self.parser.add_argument('--gpu_memory_fr', type=float, default=self._get_config_tf_mem_frc(mode))

    def _get_tf_mem_allow_set(self,mode):
        self.parser.add_argument('--gpu_memory_allow', type=bool, default=self._get_config_tf_mem_allow_set(mode))

    def _get_tf_mmt(self,mode):
        self.parser.add_argument('--momentum', type=float, default=self._get_config_tf_mmt(mode))

    def _get_dp(self,mode):
        self.parser.add_argument('--display_step', type=int, default=self._get_config_dp(mode))

    def _get_batch(self,mode):
        self.parser.add_argument('--batch', type=int, default=self._get_config_batch(mode))

    def _get_weight_path(self,mode):
        self.parser.add_argument('--weights_path', type=str, default=self._get_config_weight_path(mode))

    def _get_model_path(self,mode):
        self.parser.add_argument('--models_path', type=str, default=self._get_config_model_path(mode))

    def _get_class_num(self,mode):
        self.parser.add_argument('--class_number', type=int, default=self._get_config_class_num(mode))

    def _get_base_dir(self, mode):
        self.parser.add_argument('--base_dir', type=str, default=self._get_config_base_dir(mode))

    def _get_output_path(self, mode):
        self.parser.add_argument('--output_image_path', type=str, default=self._get_config_output_dir(mode))

    def _get_pretrained(self, mode):
        self.parser.add_argument('--pretrained_net', type=str, default=self._get_config_pretrained(mode))

    def _bn_mode(self, mode):
        self.parser.add_argument('--use_bn', type=bool, default=self._get_config_bn_mode(mode))

    def _detection_mode(self, mode):
        self.parser.add_argument('--object_mode', type=str, default=self._get_config_object_mode(mode))

    def _display_mode(self, mode):
        self.parser.add_argument('--display_mode', type=str, default=self._get_config_display_mode(mode))



    def get_args(self, mode):
        self._get_img()
        self._get_gan_patch()
        self._get_gpu(mode)
        self._get_tf_mem_frc(mode)
        self._get_tf_mem_allow_set(mode)
        self._get_dp(mode)
        self._get_batch(mode)
        self._get_weight_path(mode)
        self._get_class_num(mode)
        self._get_base_dir(mode)
        self._get_output_path(mode)
        self._get_model_path(mode)
        self._detection_mode(mode)

        if mode == 'TRAIN':
            self._get_epoch(mode)
            self._get_lr(mode)
            self._get_tf_mmt(mode)
            self._get_pretrained(mode)
            self._bn_mode(mode)
        if mode == 'TEST':
            self._display_mode(mode)



        return self.parser.parse_args()

    def log_info(self, mode):
        args = self.get_args(mode)
        # print(args.__dict__)
        [log.info('config information {} : {}'.format(elm, args.__dict__[str(elm)])) for _, elm in enumerate(args.__dict__)]




class parsing_api(globalconfig.Parsing_config):
    def __init__(self):
        super(parsing_api, self).__init__()
        self.parser = argparse.ArgumentParser(description='Data configuration and data parsing')
        # self.real = True
        # h = self._get_img_h()
        # w = self._get_img_w()
        pass

    def _get_img(self):
        self.parser.add_argument('--height', type=int, default=self._get_config_image_h())
        self.parser.add_argument('--width', type=int, default=self._get_config_image_w())
        self.parser.add_argument('--channel', type=int, default=self._get_config_image_c())


    def bgr2rgb(self, lbl):
        b, g, r = cv2.split(lbl)  # split b,g,r
        lbl = cv2.merge([r, g, b])  # bgr 2 rgb
        return lbl


    def rgb2bgr(self, lbl):
        r, g, b = cv2.split(lbl)
        lbl = cv2.merge([b, g, r])
        return lbl

    def _get_key_mode(self,mode):
        return self._get_config_mode(mode).keys()

    def _get_key_mode(self,mode):
        return self._get_config_mode(mode).keys()

    #get api
    def convert_color(self, lbl,src_mode,tar_mode):
        lbl = self.bgr2rgb(lbl)
        _get_src_key = self._get_key_mode(src_mode)

        for _, key in enumerate(_get_src_key):
            try:
                lbl[(lbl == np.asarray(self._get_config_class(src_mode,key))).all(axis=2)] = self._get_config_class(tar_mode,key)
            except KeyError:
                if key == 'TERRAIN':
                    lbl[(lbl == np.asarray(self._get_config_class(src_mode, key))).all(axis=2)] = self._get_config_class(tar_mode, 'VEGETATION')
                else:
                    lbl[(lbl == np.asarray(self._get_config_class(src_mode, key))).all(axis=2)] = self._get_config_class(tar_mode, 'UNDEFINED')


        lbl = self.rgb2bgr(lbl)

        return lbl








if __name__ == "__main__":
    parsing = parsinginterface()
    args = parsing.log_info(mode_list['TRAIN'])
    pass