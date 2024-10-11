# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py

class BasicModelWithSharedWeight(autotrackable.AutoTrackable):
    """Model with multiple functions and a shared weight."""

    def __init__(self):
        self.weight = constant_op.constant([1.0],
                                           shape=(1, 512, 512, 1),
                                           dtype=dtypes.float32)

    @def_function.function
    def add(self, x):
        exit(x + self.weight)

    @def_function.function
    def sub(self, x):
        exit(x - self.weight)

    @def_function.function
    def mul(self, x):
        exit(x * self.weight)

exit(BasicModelWithSharedWeight())
