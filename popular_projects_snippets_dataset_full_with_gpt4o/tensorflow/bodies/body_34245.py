# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
t = constant_op.constant([1.0, 2.0])
l = list_ops.tensor_list_from_tensor(t, element_shape=[])
with context.device("gpu:0"):
    l_gpu = array_ops.identity(l)
    self.assertAllEqual(
        self.evaluate(
            list_ops.tensor_list_pop_back(
                l_gpu, element_dtype=dtypes.float32)[1]), 2.0)
l_cpu = array_ops.identity(l_gpu)
self.assertAllEqual(
    self.evaluate(
        list_ops.tensor_list_pop_back(
            l_cpu, element_dtype=dtypes.float32)[1]), 2.0)
