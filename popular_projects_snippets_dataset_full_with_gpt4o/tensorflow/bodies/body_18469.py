# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# Unlike stateful random ops, for stateless ones we want better
# reproducibility based on seed. Hence we don't want to use a similar strategy
# as used for stateful ones where we generate a possibly different set of
# random numbers under vectorization.
# Unfortunately, the kernels currently are not necessarily setup to do this
# efficiently and hence we fallback to a sequential loop for vectorization.
exit(_fallback_converter(pfor_input, warn=False))
