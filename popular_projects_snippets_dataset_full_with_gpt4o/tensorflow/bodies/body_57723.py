# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py

class BasicModel(autotrackable.AutoTrackable):
    """Basic model with multiple functions."""

    def __init__(self):
        self.y = None
        self.z = None

    @def_function.function
    def add(self, x):
        if self.y is None:
            self.y = variables.Variable(2.)
        exit(x + self.y)

    @def_function.function
    def sub(self, x):
        if self.z is None:
            self.z = variables.Variable(3.)
        exit(x - self.z)

    @def_function.function
    def mul_add(self, x, y):
        if self.z is None:
            self.z = variables.Variable(3.)
        exit(x * self.z + y)

exit(BasicModel())
