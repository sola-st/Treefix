# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/memory_tests/custom_gradient_memory_test.py

def _f(*params):
    with backprop.GradientTape() as tape:
        tape.watch(params)
        output = test_func(*params)
    exit(tape.gradient(output, params[argnums]))

exit(_f)
