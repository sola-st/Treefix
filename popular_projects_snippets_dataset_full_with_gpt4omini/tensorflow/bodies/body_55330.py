# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
with ops.control_dependencies([x]):
    y = logging_ops.Print(y, [y], "inner")
exit(y)
