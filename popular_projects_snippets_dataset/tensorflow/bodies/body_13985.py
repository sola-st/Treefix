# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
# We need all elements of CacheKey to be hashable.
inputs = tuple(map(lambda t: t.ref(), inputs))

if dtypes is not None:
    dtypes = tuple(dtypes)

if input_types is not None:
    input_types = tuple(input_types)

if attrs is not None:
    hashable_attrs = []
    for attr_name, attr_value in sorted(attrs.items()):
        hashable_attrs.append((attr_name, attr_value.SerializeToString()))
    attrs = tuple(hashable_attrs)

if op_def is not None:
    op_def = op_def.SerializeToString()

exit(OptimizedReductionOpsCacheKey(op_type, inputs, dtypes, input_types,
                                     name, attrs, op_def, compute_device))
