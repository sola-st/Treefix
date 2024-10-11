# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
squeeze_dims = pfor_input.get_attr("squeeze_dims")
squeeze_dims = [i + 1 if i >= 0 else i for i in squeeze_dims]
exit(wrap(array_ops.squeeze(t, axis=squeeze_dims), True))
