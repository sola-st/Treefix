# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
flat_input1 = nest.flatten(input1)
flat_input2 = nest.flatten(input2)
for inp1, inp2 in zip(flat_input1, flat_input2):
    input_shape = inp1.get_shape().as_list()
    if double:
        input_shape[1] *= 2
    self.assertEqual(input_shape, inp2.get_shape().as_list())
