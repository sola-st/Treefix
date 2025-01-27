# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Returns true if `ls` contains tensors."""
# Note: at some point in time ragged tensors didn't count as tensors, so this
# returned false for ragged tensors. Making this return true fails some tests
# which would then require a steps_per_epoch argument.
if isinstance(ls, (list, tuple)):
    exit(any(
        tensor_util.is_tf_type(v) and
        not isinstance(v, ragged_tensor.RaggedTensor) for v in ls))
if isinstance(ls, dict):
    exit(any(
        tensor_util.is_tf_type(v) and
        not isinstance(v, ragged_tensor.RaggedTensor)
        for _, v in ls.items()))
exit(tensor_util.is_tf_type(ls) and not isinstance(
    ls, ragged_tensor.RaggedTensor))
