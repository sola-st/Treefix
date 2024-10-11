# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
worker = test_util.create_local_cluster(num_workers=1, num_ps=1)[0][0]
with ops.Graph().as_default(), session.Session(target=worker.target):
    with ops.device("/job:worker"):
        t = constant_op.constant([[1.0], [2.0]])
        l = list_ops.tensor_list_from_tensor(t, element_shape=None)
    with ops.device("/job:ps"):
        l_ps = array_ops.identity(l)
        element_shape = list_ops.tensor_list_element_shape(
            l_ps, shape_type=dtypes.int32)
    with ops.device("/job:worker"):
        element_shape = array_ops.identity(element_shape)
    self.assertEqual(self.evaluate(element_shape), -1)
