# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
"""Verifies that nodes with un-registered ops are not stripped."""
graph_def = graph_pb2.GraphDef()
node = graph_def.node.add()
node.name = "node_with_unreg_op"
node.op = "unreg_op"
node.attr["attr_1"].i = 1

meta_info_def = meta_graph_pb2.MetaGraphDef.MetaInfoDef()
meta_info_def.stripped_op_list.op.add()

with self.cached_session():
    meta_graph_def = meta_graph.create_meta_graph_def(
        meta_info_def=meta_info_def, graph_def=graph_def,
        strip_default_attrs=True)
    node_def = test_util.get_node_def_from_graph("node_with_unreg_op",
                                                 meta_graph_def.graph_def)
    self.assertEqual(node_def.attr["attr_1"].i, 1)
    self.assertTrue(meta_graph_def.meta_info_def.stripped_default_attrs)
