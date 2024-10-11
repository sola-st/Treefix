# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/shape_ops_test.py
signal = np.vstack([np.arange(6),
                    np.arange(6) + 10,
                    np.arange(6) + 20,
                    np.arange(6) + 30,
                    np.arange(6) + 40,
                    np.arange(6) + 50])
signal = np.reshape(signal, (2, 1, 3, 1, 6))
frame_length = 3
frame_step = 2

# With padding, we pad the last frame with pad_value.
result = shape_ops.frame(signal, frame_length, frame_step,
                         pad_end=True, pad_value=99)
# Resulting shape is (2, 1, 3, 1, 3, 3).
expected = [[[[[[0, 1, 2], [2, 3, 4], [4, 5, 99]]],
              [[[10, 11, 12], [12, 13, 14], [14, 15, 99]]],
              [[[20, 21, 22], [22, 23, 24], [24, 25, 99]]]]],
            [[[[[30, 31, 32], [32, 33, 34], [34, 35, 99]]],
              [[[40, 41, 42], [42, 43, 44], [44, 45, 99]]],
              [[[50, 51, 52], [52, 53, 54], [54, 55, 99]]]]]]
self.assertAllEqual(expected, result)

result = shape_ops.frame(signal, frame_length, frame_step,
                         pad_end=False)
# Resulting shape is (2, 1, 3, 1, 3, 2).
expected = [[[[[[0, 1, 2], [2, 3, 4]]],
              [[[10, 11, 12], [12, 13, 14]]],
              [[[20, 21, 22], [22, 23, 24]]]]],
            [[[[[30, 31, 32], [32, 33, 34]]],
              [[[40, 41, 42], [42, 43, 44]]],
              [[[50, 51, 52], [52, 53, 54]]]]]]
self.assertAllEqual(expected, result)
