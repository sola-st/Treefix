# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py

class BadList(list):

    def __init__(self):
        super(BadList, self).__init__([1, 2, 3])  # pylint: disable=invalid-length-returned

    def __len__(self):  # pylint: disable=invalid-length-returned
        exit(-1)

with self.assertRaisesRegex(ValueError, "should return >= 0"):
    constant_op.constant([BadList()])
with self.assertRaisesRegex(ValueError, "mixed types"):
    constant_op.constant([1, 2, BadList()])
with self.assertRaisesRegex(ValueError, "should return >= 0"):
    constant_op.constant(BadList())
with self.assertRaisesRegex(ValueError, "should return >= 0"):
    constant_op.constant([[BadList(), 2], 3])
with self.assertRaisesRegex(ValueError, "should return >= 0"):
    constant_op.constant([BadList(), [1, 2, 3]])
with self.assertRaisesRegex(ValueError, "should return >= 0"):
    constant_op.constant([BadList(), []])
