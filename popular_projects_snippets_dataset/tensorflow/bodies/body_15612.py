# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_eager_test.py
rt = ragged_factory_ops.constant(pylist)
self.assertEqual(str(rt), f'<tf.RaggedTensor {expected_str}>')
