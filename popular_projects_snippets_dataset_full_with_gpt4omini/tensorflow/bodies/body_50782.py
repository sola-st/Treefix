# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
tensor_names, shapes_and_slices, tensors, restored_trackables = (
    get_tensor_slices(trackables))
dtypes = [t.dtype for t in tensors]
restored_tensors = io_ops.restore_v2(merged_prefix, tensor_names,
                                     shapes_and_slices, dtypes)
for trackable, restored_tensor in zip(restored_trackables, restored_tensors):
    expected_shape = trackable.value().get_shape()
    restored_tensor = array_ops.reshape(restored_tensor, expected_shape)
    parts = array_ops.unstack(restored_tensor)
    for part, restored_part in zip(trackable.parts, parts):
        part.assign(restored_part)
