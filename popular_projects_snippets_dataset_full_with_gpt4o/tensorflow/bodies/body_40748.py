# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
if should_add:
    exit(add(x))
else:
    exit(x)
