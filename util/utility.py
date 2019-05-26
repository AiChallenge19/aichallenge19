import numpy as np
import os
import json

def change_mm2ai(results,CLASSES):
    ai = ['person','bicycle', 'car','motorcycle','bus','truck','fire_hydrant']
    revised_results = []
    for result, cls in zip(results,CLASSES):
        if cls in ai:
            if cls in ['bus','truck']:
                if np.size(result)>0:
                    revised_results[2] = np.concatenate([revised_results[2],result],axis=0)
            else:
                revised_results.append(result)


    return revised_results,['person','bicycle', 'car','motorcycle','fire_hydrant']

def save_object(results,cls_list):
    results_dict = dict()
    for val, cls in zip(results,cls_list):
        results_dict[cls] = []
        for i in range(val.shape[0]):
            object_info = dict()
            object_info['id'] = i
            object_info['bbox'] = val[i]
            results_dict[cls].append(object_info)
    return results_dict



class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
            np.int16, np.int32, np.int64, np.uint8,
            np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32,
            np.float64)):
            return float(obj)
        elif isinstance(obj,(np.ndarray,)): #### This is the fix
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def save2json(result,output_path,clip):
    # result = json.dumps(result,cls=NumpyEncoder, indent=4)
    save_json = os.path.join(output_path, '{:04d}'.format(clip) + '.json')
    with open(save_json, 'w') as outfile:
        json.dump(result,outfile,cls=NumpyEncoder, indent=4)
    os.chmod(save_json,0o777)



