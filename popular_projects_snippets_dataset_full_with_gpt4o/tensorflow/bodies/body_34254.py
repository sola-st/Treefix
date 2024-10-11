# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
worker = test_util.create_local_cluster(num_workers=1, num_ps=1)[0][0]
with ops.Graph().as_default(), session.Session(target=worker.target):
    with ops.device("/job:worker"):
        t = constant_op.constant([[1.0], [2.0]])
        l = list_ops.tensor_list_from_tensor(t, element_shape=[1])
    with ops.device("/job:ps"):
        l_ps = array_ops.identity(l)
        l_ps, e = list_ops.tensor_list_pop_back(
            l_ps, element_dtype=dtypes.float32)
    with ops.device("/job:worker"):
        worker_e = array_ops.identity(e)
    self.assertAllEqual(self.evaluate(worker_e), [2.0])
