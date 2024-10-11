# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
test_prediction = line_template(test_input)
exit(math_ops.reduce_mean(
    math_ops.square(test_prediction - test_output)))
