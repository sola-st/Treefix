# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
self.save_function = save_function
self.restore_function = restore_function

if tensor_util.is_tf_type(name):
    name_tensor = name
else:
    with ops.init_scope():
        name_tensor = constant_op.constant(name)
tensors = save_function(name_tensor)
specs = []
for (str_name, str_slice), tensor_info in zip(names_and_slices, tensors):
    specs.append(saveable_object.SaveSpec(tensor_info["tensor"], str_slice,
                                          name + str_name))
super(RestoredSaveableObject, self).__init__(None, specs, name)
