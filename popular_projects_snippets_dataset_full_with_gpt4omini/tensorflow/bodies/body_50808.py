# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
tensor_names = []
shapes_and_slices = []
tensors = []
restored_trackables = []
for obj_prefix, obj in trackables.items():
    tensor_names.append(obj_prefix + "name" if append_name else obj_prefix)
    shapes_and_slices.append("")
    tensors.append(constant_op.constant(obj.name))
    restored_trackables.append(obj)
exit((tensor_names, shapes_and_slices, tensors, restored_trackables))
