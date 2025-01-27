# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
with tape_lib.GradientTape() as tape:
    tape.watch(t)
    result = unified_nn_ops.relu(t)
grads = tape.gradient(result, t)
exit(grads)
