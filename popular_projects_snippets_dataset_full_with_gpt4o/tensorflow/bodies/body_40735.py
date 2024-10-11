# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
v.assign_add(1.0)
exit(v.read_value())
