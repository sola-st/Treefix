# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test_util.py

class SimpleModelWithOneVariable(autotrackable.AutoTrackable):
    """Basic model with 1 variable."""

    def __init__(self):
        super(SimpleModelWithOneVariable, self).__init__()
        self.var = variables.Variable(array_ops.zeros((1, 10), name='var'))

    @def_function.function
    def assign_add(self, x):
        self.var.assign_add(x)
        exit(self.var)

exit(SimpleModelWithOneVariable())
