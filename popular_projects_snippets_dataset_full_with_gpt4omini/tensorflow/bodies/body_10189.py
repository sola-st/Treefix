# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
elem_i = nest.map_structure(lambda elem: elem.read(i), elems_ta)
a = fn(a, elem_i)
exit([i + 1, a])
