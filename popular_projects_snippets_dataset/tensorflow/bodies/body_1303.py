# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
w.assign(w.read_value() + x)
exit(v.read_value() + x * w.read_value())
