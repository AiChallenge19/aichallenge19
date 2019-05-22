import json
import os
import glog as log


class globalconfig(object):
    def __init__(self):
        super(globalconfig, self).__init__()
        print(os.getcwd())
        self._CONFIG_PATH = 'config/globalconfig.json'
        self._check_isdir()
        # self._get_config_overall()
        # self._get_config_Network()
        # self._get_config_train()
        pass

    def _check_isdir(self):
        try:
            os.path.isdir(self._CONFIG_PATH)
            log.info('json path {} is found'.format(self._CONFIG_PATH))
            log.info('json path {} is found'.format(self._CONFIG_PATH))
        except OSError as e:
            raise e

    #get overall json data
    def _get_config_overall(self):
        with open(self._CONFIG_PATH) as json_file:
            self.config = json.load(json_file)

    # get overall image data
    def _get_config_image(self):
        self._get_config_overall()
        self._img = self.config['IMAGE']

    def _get_config_image_h(self):
        self._get_config_image()
        return self._img['HEIGHT']

    def _get_config_image_w(self):
        self._get_config_image()
        return self._img['WIDTH']

    def _get_config_image_c(self):
        self._get_config_image()
        return self._img['CHANNEL']

    # get overall pix2pix patch information
    def _get_overall_patch(self):
        self._get_config_overall()
        self._patch = self.config['pix2pix_GAN']

    def _get_img_channels(self):
        self._get_overall_patch()
        return self._patch['img_channels']

    def _get_gt_channels(self):
        self._get_overall_patch()
        return self._patch['gt_channels']

    def _get_cls_channels(self):
        self._get_overall_patch()
        return self._patch['cls_channels']

    def _get_patch_number(self):
        self._get_overall_patch()
        return self._patch['patch_number']

    def _get_patch_height(self):
        self._get_overall_patch()
        return self._patch['patch_height']

    def _get_patch_width(self):
        self._get_overall_patch()
        return self._patch['patch_width']



    # get overall network data
    def _get_config_Network(self):
        self._get_config_overall()
        return self.config['NETWORK']

    def _get_config_mode(self,mode):
        return self._get_config_Network()[mode]

    def _get_config_gpu(self,mode):
        return self._get_config_mode(mode)['GPU']

    def _get_config_epoch(self,mode):
        return self._get_config_mode(mode)['EPOCH']

    def _get_config_tf_mem_frc(self,mode):
        return self._get_config_mode(mode)['GPU_MEMORY_FRACTION']

    def _get_config_tf_mem_allow_set(self,mode):
        return self._get_config_mode(mode)['TF_ALLOW_GROWTH']

    def _get_config_tf_mmt(self,mode):
        return self._get_config_mode(mode)['MOMENTUM']

    def _get_config_train_lr(self,mode):
        return self._get_config_mode(mode)['LEARNING_RATE']

    def _get_config_dp(self,mode):
        return self._get_config_mode(mode)['DISPLAY_STEP']

    def _get_config_batch(self,mode):
        return self._get_config_mode(mode)['BATCH_SIZE']

    def _get_config_weight_path(self,mode):
        return self._get_config_mode(mode)['WEIGHT_PATH']

    def _get_config_model_path(self,mode):
        return self._get_config_mode(mode)['MODEL_PATH']

    def _get_config_class_num(self,mode):
        return self._get_config_mode(mode)['CLASSES_NUMS']

    def _get_config_base_dir(self,mode):
        return self._get_config_mode(mode)['BASE_DIR']

    def _get_config_output_dir(self,mode):
        return self._get_config_mode(mode)['OUTPUT_PATH']

    def _get_config_pretrained(self,mode):
        return self._get_config_mode(mode)['PRETRAINED_NET']

    def _get_config_bn_mode(self,mode):
        return self._get_config_mode(mode)['BN_MODE']

    def _get_config_object_mode(self,mode):
        return self._get_config_mode(mode)['OBJECT_MODE']

    def _get_config_display_mode(self,mode):
        return self._get_config_mode(mode)['DISPLAY_MODE']






if __name__ == "__main__":
    Parsing_data = Parsing_config()

    a = Parsing_data._get_config_mode(mode_list['vra']).keys()

    # pass