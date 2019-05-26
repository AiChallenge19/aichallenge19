import json
import os
import glog as log


class globalconfig(object):
    def __init__(self):
        super(globalconfig, self).__init__()
        print(os.getcwd())
        self._CONFIG_PATH = 'config/globalconfig.json'
        self._check_isdir()


    def _check_isdir(self):
        try:
            os.path.isfile(self._CONFIG_PATH)
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

    # get overall network data
    def _get_config_Network(self):
        self._get_config_overall()
        return self.config['NETWORK']

    def _get_config_mode(self,mode):
        return self._get_config_Network()[mode]

    def _get_config_gpu(self,mode):
        return self._get_config_mode(mode)['GPU']

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

