# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/qr_op_test.py
with backprop.GradientTape() as tape:
    tape.watch(x)
    ret = linalg_ops.qr(x, full_matrices=True)
exit(tape.gradient(ret, x))
