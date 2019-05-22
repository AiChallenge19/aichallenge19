import glog as log
from config.parsinginterface import *


def log_info_args(mode):
    parsinginterface().log_info(mode)

def inform_finish_inference():
    log.info("finish this folders")

def get_config_args(mode):
    log_info_args(mode)
    return parsinginterface().get_args(mode)

def log_info_time(tag,time):
    log.info("{} time is {}sec".format(tag,time))

def log_info_elapsed_time(tag,elapsed_time):
    log.info("{} time is {}sec".format(tag,elapsed_time))

def log_info_step(tag,time,one_step,total_step,num):
    log.info("{} time is {}sec/step ({} / {} steps) in this {}th sequence".format(tag,time,one_step,total_step,num))

def log_info_total(tag,elapsed_time,total_num):
    log.info("{} time is {}sec (total img number : {})".format(tag,elapsed_time,total_num))