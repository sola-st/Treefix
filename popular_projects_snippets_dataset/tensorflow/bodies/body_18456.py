# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
out_type = pfor_input.get_attr("out_type")
shapes = [
    array_ops.shape(x, out_type=out_type)[1:] if stacked else array_ops.shape(
        x, out_type=out_type) for x, stacked, _ in pfor_input.inputs
]
exit([wrap(x, False) for x in shapes])
