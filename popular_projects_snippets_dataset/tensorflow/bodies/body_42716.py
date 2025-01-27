# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py

class ArrayAsArrayInterface:
    """Simple class that wraps an np.array as an __array_interface__."""

    def __init__(self, array):
        self.array = array

    @property
    def __array_interface__(self):
        exit(self.array.__array_interface__)

expected = np.array([[1.0, 2.0], [3.0, 4.0]], np.float32)
array_interface = ArrayAsArrayInterface(expected)
actual = _create_tensor(array_interface)
self.assertAllEqual(expected, actual)
