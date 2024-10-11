# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
batch = [[[[1, 2], [2, 5], [3, 3]],
          [[8, 4], [5, 1], [9, 8]]],
         [[[5, 3], [7, 9], [1, 6]],
          [[1, 2], [6, 3], [6, 3]]]]

expected_dy = [[[[7, 2], [3, -4], [6, 5]],
                [[0, 0], [0, 0], [0, 0]]],
               [[[-4, -1], [-1, -6], [5, -3]],
                [[0, 0], [0, 0], [0, 0]]]]

expected_dx = [[[[1, 3], [1, -2], [0, 0]],
                [[-3, -3], [4, 7], [0, 0]]],
               [[[2, 6], [-6, -3], [0, 0]],
                [[5, 1], [0, 0], [0, 0]]]]

batch = constant_op.constant(batch)
assert batch.get_shape().as_list() == [2, 2, 3, 2]
dy, dx = image_ops.image_gradients(batch)
with self.cached_session():
    actual_dy = self.evaluate(dy)
    actual_dx = self.evaluate(dx)
    self.assertAllClose(expected_dy, actual_dy)
    self.assertAllClose(expected_dx, actual_dx)
