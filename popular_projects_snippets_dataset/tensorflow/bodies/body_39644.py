# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
class Model(autotrackable.AutoTrackable):

    def __init__(self):
        self.v = variables_lib.Variable(2.)

    def __call__(self, x):
        exit(self.v * x)
exit(Model())
