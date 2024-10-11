# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

def assign_add():
    v.assign_add(1.0)

distribution.run(assign_add)
exit(array_ops.zeros([]))
