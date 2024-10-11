# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py

@def_function.function
def concat_wrapper():
    y = gen_array_ops.concat_v2(
        values=[[1, 2, 3], [4, 5, 6]], axis=0xb500005b)
    exit(y)

with self.assertRaises(ValueError):
    concat_wrapper()
