# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv_node_name_test.py
input_sizes = [8, 16, 3]
filter_sizes = [7]
strides = 1
dilations = [2]
layer = layers.Conv1D
self._verifyNodeNameMatch(layer, input_sizes, filter_sizes, strides,
                          dilations)
