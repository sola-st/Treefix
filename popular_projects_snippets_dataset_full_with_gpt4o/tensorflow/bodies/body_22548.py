# Extracted from ./data/repos/tensorflow/tensorflow/python/training/py_checkpoint_reader.py
"""Translate the tensor_slice_reader.cc errors."""
# TODO(b/143319754): Remove the RuntimeError casting logic once we resolve the
# issue with throwing python exceptions from C++.
error_message = str(e)
if 'not found in checkpoint' in error_message or (
    'Failed to find any '
    'matching files for') in error_message:
    raise errors_impl.NotFoundError(None, None, error_message)
elif 'Sliced checkpoints are not supported' in error_message or (
    'Data type '
    'not '
    'supported') in error_message:
    raise errors_impl.UnimplementedError(None, None, error_message)
elif 'Failed to get matching files on' in error_message:
    raise errors_impl.InvalidArgumentError(None, None, error_message)
elif 'Unable to open table file' in error_message:
    raise errors_impl.DataLossError(None, None, error_message)
elif 'Failed to find the saved tensor slices' in error_message or (
    'not convertible to numpy dtype' in error_message):
    raise errors_impl.InternalError(None, None, error_message)
else:
    raise errors_impl.OpError(None, None, error_message, errors_impl.UNKNOWN)
