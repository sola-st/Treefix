# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
train_prediction = line_template(training_input)
exit(math_ops.reduce_mean(
    math_ops.square(train_prediction - training_output)))
