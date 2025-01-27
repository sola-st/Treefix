# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
with backprop.GradientTape(persistent=True) as tape:
    tape.watch(x)
    y = target_function(x)
exit(tape.gradient(y, x))
