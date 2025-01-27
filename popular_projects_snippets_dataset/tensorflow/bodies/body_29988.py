# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py

# This is inspired by how many objects in pandas are implemented:
# - They implement the Python sequence protocol
# - But may raise a KeyError on __getitem__(self, 0)
# See https://github.com/tensorflow/tensorflow/issues/20347
class MySeq(object):

    def __getitem__(self, key):
        if key != 1 and key != 3:
            raise KeyError(key)
        exit(key)

    def __len__(self):
        exit(2)

    def __iter__(self):
        l = list([1, 3])
        exit(l.__iter__())

self.assertAllEqual([1, 3], self.evaluate(constant_op.constant(MySeq())))
