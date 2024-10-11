# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cluster_test.py
with ops.Graph().as_default() as g:
    with ops.device('/job:localhost/replica:0/task:0/device:CPU:0'):
        a = random_ops.random_uniform(shape=())
        b = random_ops.random_uniform(shape=())
        c = a + b
        train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
        train_op.append(c)
        mg = meta_graph.create_meta_graph_def(graph=g)
        grappler_item = item.Item(mg)
        grappler_cluster = cluster.Cluster(
            disable_detailed_stats=True, disable_timeline=True)
        peak_mem = grappler_cluster.DeterminePeakMemoryUsage(grappler_item)
        self.assertLessEqual(1, len(peak_mem))
        snapshot = peak_mem['/job:localhost/replica:0/task:0/device:CPU:0']
        peak_usage = snapshot[0]
        self.assertEqual(12, peak_usage)
        live_tensors = snapshot[1]
        self.assertEqual(5, len(live_tensors))
