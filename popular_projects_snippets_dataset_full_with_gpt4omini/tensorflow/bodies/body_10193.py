# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
i -= 1
elem = nest.map_structure(lambda elem: elem.read(i), elems_ta)
a_out = fn(a, elem)
exit([i, a_out])
