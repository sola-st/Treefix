# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py

class NoInit(autotrackable.AutoTrackable):

    def __init__(self):
        pass

    # __init__ for Trackable will be called implicitly.
trackable_utils.add_variable(NoInit(), "var", shape=[])
