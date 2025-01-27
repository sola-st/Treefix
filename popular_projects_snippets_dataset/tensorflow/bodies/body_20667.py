# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/cluster_test.py
with ops.Graph().as_default() as g:
    a = random_ops.random_uniform(shape=())
    b = random_ops.random_uniform(shape=())
    c = a + b
    train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
    train_op.append(c)
    mg = meta_graph.create_meta_graph_def(graph=g)
    grappler_item = item.Item(mg)

with cluster.Provision(
    disable_detailed_stats=False, disable_timeline=False) as gcluster:
    op_perfs, run_time, step_stats = gcluster.MeasureCosts(grappler_item)
    self.assertTrue(run_time > 0)
    self.assertEqual(len(op_perfs), 4)
    self.assertTrue(step_stats.dev_stats)
