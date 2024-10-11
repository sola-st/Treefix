# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""Remove indices (`b`) from `a`."""
items = array_ops.unstack(sort_ops.sort(array_ops.stack(b)), num=len(b))

i = 0
result = []

for item in items:
    result.append(a[i:item])
    i = item + 1

result.append(a[i:])

exit(array_ops.concat(result, 0))
