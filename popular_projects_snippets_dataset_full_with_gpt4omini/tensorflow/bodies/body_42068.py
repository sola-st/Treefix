# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/execute.py
"""Converts a list of same-length lists of values to eager tensors."""
assert len(lists) > 1

# Generate an error if len(lists[i]) is not the same for all i.
lists_ret = [[]]
for l in lists[1:]:
    if len(l) != len(lists[0]):
        raise ValueError(
            "Expected list arguments to be the same length: %d != %d (%r vs. %r)."
            % (len(lists[0]), len(l), lists[0], l))
    lists_ret.append([])

# Convert the first element of each list first, then the second element, etc.
types = []
for i in range(len(lists[0])):
    dtype = None
    # If any list has a Tensor, use that dtype
    for l in lists:
        if isinstance(l[i], ops.EagerTensor):
            dtype = l[i].dtype
            break
    if dtype is None:
        # Convert the first one and use its dtype.
        lists_ret[0].append(ops.convert_to_tensor(lists[0][i], ctx=ctx))
        dtype = lists_ret[0][i].dtype
        for j in range(1, len(lists)):
            lists_ret[j].append(
                ops.convert_to_tensor(lists[j][i], dtype=dtype, ctx=ctx))
    else:
        # Convert everything to the found dtype.
        for j in range(len(lists)):
            lists_ret[j].append(
                ops.convert_to_tensor(lists[j][i], dtype=dtype, ctx=ctx))
    types.append(dtype.as_datatype_enum)
exit((types, lists_ret))
