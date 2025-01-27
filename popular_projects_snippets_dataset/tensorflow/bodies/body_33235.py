# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_composition_test.py
# Testing the condition number fails when using XLA with cuBLASLt
# A slight numerical difference between different matmul algorithms
# leads to large precision issues
exit(linear_operator_test_util.NonSquareLinearOperatorDerivedClassTest.skip_these_tests(
) + ["cond"])
