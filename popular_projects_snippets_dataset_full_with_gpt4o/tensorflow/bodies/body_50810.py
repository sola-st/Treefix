# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration_saving_test.py
tensor_names, shapes_and_slices, tensors, restored_trackables = (
    _get_tensors(trackables))
dtypes = [t.dtype for t in tensors]
try:
    restored_tensors = io_ops.restore_v2(merged_prefix, tensor_names,
                                         shapes_and_slices, dtypes)
except errors_impl.NotFoundError:
    # If a NotFoundError is caught, then it means that the checkpoint
    # was written prior to the saver registration migration.
    tensor_names, shapes_and_slices, tensors, restored_trackables = (
        _get_tensors(trackables, append_name=False))
    restored_tensors = io_ops.restore_v2(merged_prefix, tensor_names,
                                         shapes_and_slices, dtypes)
for trackable, name_tensor in zip(restored_trackables, restored_tensors):
    trackable.name = name_tensor
