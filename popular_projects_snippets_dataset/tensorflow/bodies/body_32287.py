# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/shape_ops_test.py
signal = np.reshape(np.arange(16), (2, 4, 2))
result = shape_ops.frame(signal, frame_length=2, frame_step=2,
                         pad_end=True, axis=1)
expected = np.reshape(np.arange(16), (2, 2, 2, 2))
self.assertAllEqual(expected, self.evaluate(result))

result = shape_ops.frame(signal, frame_length=2, frame_step=1,
                         pad_end=True, axis=1)
expected = [[[[0, 1], [2, 3]],
             [[2, 3], [4, 5]],
             [[4, 5], [6, 7]],
             [[6, 7], [0, 0]]],
            [[[8, 9], [10, 11]],
             [[10, 11], [12, 13]],
             [[12, 13], [14, 15]],
             [[14, 15], [0, 0]]]]
self.assertAllEqual(expected, self.evaluate(result))

result = shape_ops.frame(signal, frame_length=3, frame_step=1,
                         pad_end=True, axis=1)
expected = [[[[0, 1], [2, 3], [4, 5]],
             [[2, 3], [4, 5], [6, 7]],
             [[4, 5], [6, 7], [0, 0]],
             [[6, 7], [0, 0], [0, 0]]],
            [[[8, 9], [10, 11], [12, 13]],
             [[10, 11], [12, 13], [14, 15]],
             [[12, 13], [14, 15], [0, 0]],
             [[14, 15], [0, 0], [0, 0]]]]
self.assertAllEqual(expected, self.evaluate(result))
