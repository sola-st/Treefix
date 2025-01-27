# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test.py
with ops.Graph().as_default() as g:
    tpu.rewrite(do_einsum)
    self.assertTrue(find_einsum(g) or find_xla_einsum(g))
