# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_loops_test.py
train_fn.counter += 1
if train_fn.counter == 3:
    raise RuntimeError("Failed")
