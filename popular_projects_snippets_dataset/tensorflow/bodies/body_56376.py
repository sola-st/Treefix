# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
with ops.device('/device:GPU:0'):
    exit(test_ops.test_attr(T=dtypes.float32, name='test_attr'))
