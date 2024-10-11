# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_operators_test.py
a = ragged_factory_ops.constant([[True, True], [False]])
with self.assertRaisesRegex(TypeError,
                            'RaggedTensor may not be used as a boolean.'):
    bool(a)
with self.assertRaisesRegex(TypeError,
                            'RaggedTensor may not be used as a boolean.'):
    if a:
        pass
