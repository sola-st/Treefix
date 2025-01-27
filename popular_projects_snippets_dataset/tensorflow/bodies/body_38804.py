# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/gradient_correctness_test.py
with test_util.AbstractGradientTape(use_tape=use_tape) as tape:
    k = constant_op.constant([3, 4])
    tape.watch(k)

    m = k * k
    n = m * m
    dn_dk = tape.gradient(n, k)
    self.assertIsNone(dn_dk)
