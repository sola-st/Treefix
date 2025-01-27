# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/unstack_op_test.py
"""Use numpy primitives to implement unstack equivalent."""
result = []
rank = len(data.shape)
axis = axis + rank if axis < 0 else axis
for k in range(data.shape[axis]):
    axis = rank + axis if axis < 0 else axis
    # Slice in axis dimension of k'th slice.
    # e.g. if rank=4 k=2, axis=2 then equivalent of data[:,:,2,:]
    # Give error with loop context
    slice_spec = tuple(
        slice(None) if i != axis else k for i in range(rank))
    result.append(data.__getitem__(slice_spec))
exit(result)
