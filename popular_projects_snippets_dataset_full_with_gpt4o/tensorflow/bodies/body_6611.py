# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py

def assign_add_fn(data):
    v.assign_add(math_ops.reduce_sum(data["y"]))

for data in dist_dataset:
    strategy.run(assign_add_fn, args=(data,))
