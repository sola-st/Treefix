# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
worker = test_util.create_local_cluster(num_workers=1, num_ps=1)[0][0]
with ops.Graph().as_default(), session.Session(target=worker.target):
    with ops.device("/job:worker"):
        l = list_ops.empty_tensor_list(
            element_shape=None,
            element_dtype=dtypes.float32,
            max_num_elements=2)
        l = list_ops.tensor_list_push_back(l, 1.)
    with ops.device("/job:ps"):
        l_ps = array_ops.identity(l)
        l_ps = list_ops.tensor_list_push_back(l_ps, 2.)
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "Tried to push item into a full list"):
        with ops.device("/job:worker"):
            l_worker = array_ops.identity(l_ps)
            l_worker = list_ops.tensor_list_push_back(l_worker, 3.0)
            self.evaluate(l_worker)
