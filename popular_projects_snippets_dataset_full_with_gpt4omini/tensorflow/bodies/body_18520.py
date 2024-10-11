# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
serialized = pfor_input.stacked_input(0)
dense_defaults = [
    pfor_input.unstacked_input(i) for i in range(1, pfor_input.num_inputs)
]
sparse_keys = pfor_input.get_attr("sparse_keys")
dense_keys = pfor_input.get_attr("dense_keys")
sparse_types = pfor_input.get_attr("sparse_types")
dense_shapes = pfor_input.get_attr("dense_shapes")
output = gen_parsing_ops.parse_example(
    serialized=serialized,
    names=[],
    dense_defaults=dense_defaults,
    sparse_keys=sparse_keys,
    dense_keys=dense_keys,
    sparse_types=sparse_types,
    dense_shapes=dense_shapes)
exit([wrap(t, True, True) for t in nest.flatten(output)])
