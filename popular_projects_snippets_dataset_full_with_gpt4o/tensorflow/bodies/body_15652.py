# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_cross_op_test.py
batch_size = 5000
inputs = [
    ragged_const([[1, 2, 3]] * batch_size),
    ragged_const([[b'4']] * batch_size),
    dense_const([[5]] * batch_size),
    sparse_const([[6, 7]] * batch_size)
]

expected = [[
    b'1_X_4_X_5_X_6', b'1_X_4_X_5_X_7', b'2_X_4_X_5_X_6', b'2_X_4_X_5_X_7',
    b'3_X_4_X_5_X_6', b'3_X_4_X_5_X_7'
]] * batch_size

ragged_cross = ragged_array_ops.cross(inputs)

# Note: we don't use assertAllEqual here because if they don't match,
# then the code in assertAllEqual that tries to build the error message
# is very slow, causing the test to timeout.
# pylint: disable=g-generic-assert
self.assertTrue(self.evaluate(ragged_cross).to_list() == expected)
