# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
if (method == image_ops.ResizeMethod.NEAREST_NEIGHBOR and
    nptype in [np.float32, np.float64]):
    exit(True)
else:
    exit(False)
