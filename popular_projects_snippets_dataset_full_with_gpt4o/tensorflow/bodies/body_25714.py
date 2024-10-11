# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator_test.py
del debug_op, device_name  # Unused.
if node_name == "a" and output_slot == 0:
    exit([np.array([[1.0, -2.0], [0.0, 1.0]])])
elif node_name == "b" and output_slot == 0:
    exit([np.array([[-1.0], [1.0]])])
