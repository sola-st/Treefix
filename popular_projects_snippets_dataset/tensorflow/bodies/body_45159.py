# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/conditional_expressions_test.py
y = x * x if x > 0 else x if x else 1
exit(y)
