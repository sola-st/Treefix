# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_flex_test.py
# Control flow is needed to generate "FlexReadVariableOp".
if tf.reduce_mean(x) > 1.0:
    self.v.assign_add([[1.0, 1.0, 1.0, 1.0]])
exit(self.v + x)
