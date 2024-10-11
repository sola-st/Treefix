# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_eager_test.py
rt = ragged_factory_ops.constant(pylist, ragged_rank)
self.assertAllEqual(rt, pylist)
