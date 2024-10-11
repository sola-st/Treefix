# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/item_test.py
with ops.Graph().as_default() as g:
    a = constant_op.constant(10)
    b = constant_op.constant(20)
    c = a + b
    train_op = ops.get_collection_ref(ops.GraphKeys.TRAIN_OP)
    train_op.append(c)
    mg = meta_graph.create_meta_graph_def(graph=g)
    grappler_item = item.Item(mg)

initial_tf_item = grappler_item.tf_item
no_change_tf_item = grappler_item.tf_item
self.assertEqual(initial_tf_item, no_change_tf_item)

# Modify the placement.
for node in grappler_item.metagraph.graph_def.node:
    node.device = '/cpu:0'
new_tf_item = grappler_item.tf_item
self.assertNotEqual(initial_tf_item, new_tf_item)

# Assign the same placement.
for node in grappler_item.metagraph.graph_def.node:
    node.device = '/cpu:0'
newest_tf_item = grappler_item.tf_item
self.assertEqual(new_tf_item, newest_tf_item)
