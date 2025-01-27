# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
labels = [
    [3, 4, 3],
    [1, 0, 0],
]
num_labels = 8

# 3 frames, 2 batch, 8 states (4 label, 4 blank).
#
# There is only single valid path for each sequence because the frame
# lengths and the label lengths are the same.
states = [[[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
           [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
          [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
           [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
          [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
           [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]]
labels = ops.convert_to_tensor(labels)
states = math_ops.log(states)
olabel = ctc_ops._state_to_olabel_unique(labels, num_labels, states,
                                         ctc_ops.ctc_unique_labels(labels))
olabel = math_ops.exp(olabel)
blank = olabel[:, :, 0]

self.assertAllClose(blank, [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]])
self.assertAllClose(olabel[:, :, 1:],
                    [
                        [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                         [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
                        [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
                        [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
                    ])
