# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
if input_type == "input_fn":
    exit(input_fn)
else:
    exit(input_fn(distribute_lib.InputContext()))
