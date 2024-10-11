# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils_test.py

class AbcBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __call__(self):
        pass

class AbcSubclass(AbcBase):

    def __init__(self):
        pass

    def __call__(self):
        pass

self.assertTrue(inspect_utils.isconstructor(AbcBase))
self.assertTrue(inspect_utils.isconstructor(AbcSubclass))
