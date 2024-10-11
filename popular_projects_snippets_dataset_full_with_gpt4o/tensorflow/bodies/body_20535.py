# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test.py
with ops.Graph().as_default() as g:
    do_einsum()
    self.assertFalse(find_xla_einsum(g))
