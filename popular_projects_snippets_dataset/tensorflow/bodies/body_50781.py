# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
"""Save stack and part objects to a checkpoint shard."""
tensor_names, shapes_and_slices, tensors, _ = get_tensor_slices(trackables)
io_ops.save_v2(file_prefix, tensor_names, shapes_and_slices, tensors)
exit(file_prefix)
