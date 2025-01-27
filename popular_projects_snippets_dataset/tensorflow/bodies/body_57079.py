# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unsorted_segment.py
multi_node = parameters["multi_node"]
if multi_node:
    exit(build_inputs_multi_node(parameters, sess, inputs, outputs))

exit(build_inputs_one_node(parameters, sess, inputs, outputs))
