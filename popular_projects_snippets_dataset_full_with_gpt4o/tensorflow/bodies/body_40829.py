# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
exit(x + math_ops.add_n(list(args) + list(kwargs.values())))
