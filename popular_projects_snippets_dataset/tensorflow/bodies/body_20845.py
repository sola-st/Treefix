# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/remapper_test.py
ops.add_to_collection('train_op', model_fn)
mg = meta_graph.create_meta_graph_def(graph=model_fn.graph)

# Compute referene
config = _get_config(remapping_on=False)
gdef_ref = tf_optimizer.OptimizeGraph(config, mg)

# Compute with remapping ON
config = _get_config(remapping_on=True)
gdef = tf_optimizer.OptimizeGraph(config, mg)

self.assertEqual(len(gdef_ref.node), len(gdef.node))
self.assertAllEqual([n.op for n in gdef_ref.node],
                    [n.op for n in gdef.node])
