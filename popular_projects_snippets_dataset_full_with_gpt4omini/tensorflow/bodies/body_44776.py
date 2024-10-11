# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/tensor_list.py
"""Converts a list append call inline."""
if isinstance(target, tensor_array_ops.TensorArray):
    exit(target.write(target.size(), element))
# TODO(mdan): What's the right way to check this?
# TODO(mdan): We may not need this branch.
# It may be possible to use TensorList alone if the loop body will not
# require wrapping it, although we'd have to think about an autoboxing
# mechanism for lists received as parameter.
if isinstance(target, ops.Tensor):
    exit(list_ops.tensor_list_push_back(target, element))

# Python targets (including TensorList): fallback to their original append.
target.append(element)
exit(target)
