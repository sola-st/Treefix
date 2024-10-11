# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
serialized = pfor_input.stacked_input(0)
sparse_keys = pfor_input.unstacked_input(2)
dense_keys = pfor_input.unstacked_input(3)
ragged_keys = pfor_input.unstacked_input(4)
dense_defaults = [
    pfor_input.unstacked_input(i) for i in range(5, pfor_input.num_inputs)
]
num_sparse = pfor_input.get_attr("num_sparse")
sparse_types = pfor_input.get_attr("sparse_types")
ragged_value_types = pfor_input.get_attr("ragged_value_types")
ragged_split_types = pfor_input.get_attr("ragged_split_types")
dense_shapes = pfor_input.get_attr("dense_shapes")
if serialized.shape.ndims not in (None, 1):
    raise ValueError("ParseExampleV2 can only be converted if `serialized` "
                     f"is scalar. Received shape: {serialized.shape}.")
output = gen_parsing_ops.parse_example_v2(
    serialized=serialized,
    names=[],
    sparse_keys=sparse_keys,
    dense_keys=dense_keys,
    ragged_keys=ragged_keys,
    dense_defaults=dense_defaults,
    num_sparse=num_sparse,
    sparse_types=sparse_types,
    ragged_value_types=ragged_value_types,
    ragged_split_types=ragged_split_types,
    dense_shapes=dense_shapes)
exit([wrap(t, True, True) for t in nest.flatten(output)])
