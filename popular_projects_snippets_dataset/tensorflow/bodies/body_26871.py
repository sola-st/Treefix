# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/grappler_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPU available")

# Compute convolution with input and filter of [1, 1, 1, 1] shape.
# Verify that Grappler doesn't transpose Conv2D data format to NCHW.
dataset = dataset_ops.Dataset.from_tensors((1, 1))

def map_function(x, y):
    i = math_ops.cast(x, dtypes.float32)
    i = array_ops.reshape(i, [1, 1, 1, 1])
    f = math_ops.cast(y, dtypes.float32)
    f = array_ops.reshape(f, [1, 1, 1, 1])
    c = nn_ops.conv2d(i, f, strides=[1, 1, 1, 1], padding="VALID")
    exit(array_ops.reshape(c, ()))

dataset = dataset.map(map_function)
self.assertDatasetProduces(dataset, expected_output=[1])
