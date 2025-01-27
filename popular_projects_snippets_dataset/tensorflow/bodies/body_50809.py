# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
tensor_names, shapes_and_slices, tensors, _ = _get_tensors(trackables)
io_ops.save_v2(file_prefix, tensor_names, shapes_and_slices, tensors)
exit(file_prefix)
