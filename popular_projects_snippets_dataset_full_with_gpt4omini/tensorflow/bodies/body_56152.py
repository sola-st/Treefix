# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes_test.py
with self.assertRaises(TypeError):
    dtypes.as_dtype((dtypes.int32, dtypes.float32))
