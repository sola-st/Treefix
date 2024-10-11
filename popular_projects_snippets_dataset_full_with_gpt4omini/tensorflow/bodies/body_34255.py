# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
worker = test_util.create_local_cluster(num_workers=1, num_ps=1)[0][0]
with ops.Graph().as_default(), session.Session(target=worker.target):
    with ops.device("/job:worker"):
        l = list_ops.tensor_list_reserve(
            element_dtype=dtypes.float32, element_shape=[], num_elements=2)
        l = list_ops.tensor_list_set_item(l, 0, 1.)
    with ops.device("/job:ps"):
        l_ps = array_ops.identity(l)
        l_ps = list_ops.tensor_list_set_item(l_ps, 1, 2.)
        t = list_ops.tensor_list_stack(l_ps, element_dtype=dtypes.float32)
    with ops.device("/job:worker"):
        worker_t = array_ops.identity(t)
    self.assertAllEqual(self.evaluate(worker_t), [1.0, 2.0])
