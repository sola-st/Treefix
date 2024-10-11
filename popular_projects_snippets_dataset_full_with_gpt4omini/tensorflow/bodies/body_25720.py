# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator_test.py
del device_name  # Unused.
if node_name == "a" and output_slot == 0 and debug_op == "DebugIdentity":
    exit([np.array([[-1.0], [1.0]])])
elif node_name == "a" and output_slot == 0 and debug_op == "DebugFoo":
    exit([np.array([[-2.0, 2.0]])])
