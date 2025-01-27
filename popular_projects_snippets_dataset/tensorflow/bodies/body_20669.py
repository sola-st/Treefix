# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cluster_test.py
with ops.Graph().as_default() as g:
    a = random_ops.random_uniform(shape=(2, 3))
    b = random_ops.random_uniform(shape=(2, 3))
    c = a + b
    dims = math_ops.range(0, array_ops.rank(c), 1)
    d = math_ops.reduce_sum(a, axis=dims)
    train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
    train_op.append(d)
    mg = meta_graph.create_meta_graph_def(graph=g)
    grappler_item = item.Item(mg)

    device_properties = device_properties_pb2.DeviceProperties(
        type='GPU', frequency=1000, num_cores=60)
    named_gpu = device_properties_pb2.NamedDevice(
        properties=device_properties, name='/GPU:0')
    device_properties = device_properties_pb2.DeviceProperties(
        type='CPU', frequency=3000, num_cores=6)
    named_cpu = device_properties_pb2.NamedDevice(
        properties=device_properties, name='/CPU:0')
    virtual_cluster = cluster.Cluster(devices=[named_cpu, named_gpu])
    supported_dev = virtual_cluster.GetSupportedDevices(grappler_item)
    self.assertEqual(supported_dev['add'], ['/CPU:0', '/GPU:0'])
    self.assertEqual(supported_dev['Sum'], ['/CPU:0', '/GPU:0'])
    self.assertEqual(supported_dev['range'], ['/CPU:0', '/GPU:0'])

    real_cluster = cluster.Cluster()
    supported_dev = real_cluster.GetSupportedDevices(grappler_item)
    if test.is_gpu_available():
        self.assertEqual(supported_dev['add'], [
            '/job:localhost/replica:0/task:0/device:CPU:0',
            '/job:localhost/replica:0/task:0/device:GPU:0'
        ])
        self.assertEqual(supported_dev['Sum'], [
            '/job:localhost/replica:0/task:0/device:CPU:0',
            '/job:localhost/replica:0/task:0/device:GPU:0'
        ])
        # The axis tensor must reside on the host
        self.assertEqual(supported_dev['range'],
                         ['/job:localhost/replica:0/task:0/device:CPU:0'])
    else:
        self.assertEqual(supported_dev['add'],
                         ['/job:localhost/replica:0/task:0/device:CPU:0'])
