# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
inp_data = ragged_factory_ops.constant(
    [['omar', 'stringer', 'marlo', 'wire'], ['marlo', 'skywalker', 'wire']],
    dtype=dtypes.string)
mask = math_ops.equal(inp_data, '')
values = string_ops.string_to_hash_bucket_strong(
    inp_data, 3, name='hash', key=[0xDECAFCAFFE, 0xDECAFCAFFE])
values = math_ops.add(values, array_ops.ones_like(values))
local_zeros = array_ops.zeros_like(values)
values = array_ops.where(mask, local_zeros, values)
