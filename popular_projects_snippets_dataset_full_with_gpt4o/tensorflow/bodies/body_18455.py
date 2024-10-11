# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
out_type = pfor_input.get_attr("out_type")
exit(wrap(
    array_ops.shape(pfor_input.stacked_input(0), out_type=out_type)[1:],
    False))
