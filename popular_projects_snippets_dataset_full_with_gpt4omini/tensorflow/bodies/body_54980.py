# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util_test.py

super(UniquePtrTest, self).setUp()

class MockClass:

    def __init__(self):
        self.deleted = False

def deleter(obj):
    obj.deleted = True

self.obj = MockClass()
self.deleter = deleter
