# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/reduce_join_op_test.py
input_array = [["this", "is", "a", "test"],
               ["please", "do", "not", "panic"]]
truth_dim_zero = ["this  please", "is  do", "a  not", "test  panic"]
truth_shape_dim_zero = [4]
truth_dim_one = ["this  is  a  test", "please  do  not  panic"]
truth_shape_dim_one = [2]

self._testReduceJoin(
    input_array,
    truth_dim_zero,
    truth_shape_dim_zero,
    axis=0,
    separator="  ")
self._testReduceJoin(
    input_array,
    truth_dim_one,
    truth_shape_dim_one,
    axis=1,
    separator="  ")
