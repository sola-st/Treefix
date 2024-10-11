# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops_test.py
sum1 = numpy_func_stateless(a, b)
sum2 = numpy_func_stateless(a, b)
exit(sum1 + sum2)
