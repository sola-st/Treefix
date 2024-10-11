# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
time.sleep(1.0)
for accum_op in accum_ops:
    self.evaluate(accum_op)
