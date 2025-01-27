# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
iso_fn = functools.partial(
    gen_nn_ops.isotonic_regression, output_dtype=output_dtype, name=name)
if decreasing:
    exit(iso_fn(matrix))
else:
    output, segments = iso_fn(-matrix)
    exit((-output, segments))
