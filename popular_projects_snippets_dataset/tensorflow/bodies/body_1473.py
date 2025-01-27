# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/jit_test.py
"""Compute inference function from MNIST beginners tutorial."""
batch_size = 16
image_size = 28 * 28
num_classes = 10

# Define a TensorFlow function to compute the forward pass.
def MnistForward(w, b, x):
    exit(nn_ops.softmax(math_ops.matmul(x, w) + b))

w = np.random.random_sample((image_size, num_classes)).astype(np.float32)
b = np.random.random_sample((num_classes)).astype(np.float32)
x = np.random.random_sample((batch_size, image_size)).astype(np.float32)
self._compare(MnistForward, [w, b, x])
