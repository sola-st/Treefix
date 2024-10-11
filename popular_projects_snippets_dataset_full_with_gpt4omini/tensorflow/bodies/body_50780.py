# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
tensor_names = []
shapes_and_slices = []
tensors = []
restored_trackables = []
for obj_prefix, obj in trackables.items():
    if isinstance(obj, Part):
        continue  # only save stacks
    tensor_names.append(obj_prefix + "/value")
    shapes_and_slices.append("")
    x = obj.value()
    with ops.device("/device:CPU:0"):
        tensors.append(array_ops.identity(x))
    restored_trackables.append(obj)

exit((tensor_names, shapes_and_slices, tensors, restored_trackables))
