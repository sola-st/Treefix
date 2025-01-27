# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cluster_test.py
with ops.Graph().as_default() as g:
    with ops.device('/device:GPU:0'):
        a = random_ops.random_uniform(shape=[1024, 1024])
        b = random_ops.random_uniform(shape=[1024, 1024])
        c = a + b
    train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
    train_op.append(c)
    mg = meta_graph.create_meta_graph_def(graph=g)
    grappler_item = item.Item(mg)
    device_properties = device_properties_pb2.DeviceProperties(
        type='GPU',
        frequency=1000,
        num_cores=60,
        environment={'architecture': '7'})
    named_device = device_properties_pb2.NamedDevice(
        properties=device_properties, name='/device:GPU:0')
    grappler_cluster = cluster.Cluster(
        disable_detailed_stats=False,
        disable_timeline=False,
        devices=[named_device])
    op_perfs, run_time, _ = grappler_cluster.MeasureCosts(grappler_item)
    self.assertEqual(run_time, 0.000209)
    self.assertEqual(len(op_perfs), 5)

    estimated_perf = grappler_cluster.EstimatePerformance(named_device)
    self.assertEqual(7680.0, estimated_perf)
