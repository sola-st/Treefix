# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
obj_type = type(obj)
exit((hasattr(obj_type, 'trainable_weights') and
        hasattr(obj_type, 'non_trainable_weights') and
        not isinstance(obj, type)))
