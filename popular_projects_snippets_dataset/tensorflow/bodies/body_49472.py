# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
for module in modules:
    for name in dir(module):
        obj = getattr(module, name)
        if obj_filter(obj):
            target_dict[name] = obj
