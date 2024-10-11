# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
"""Importing can call _TileShape without shape of <multiples> known."""
with self.cached_session():
    inp = array_ops.placeholder(dtypes.float32)  # unknown shape
    multiples = constant_op.constant([1, 2, 3, 4], dtype=np.int32)
    tiled = array_ops.tile(inp, multiples)
    gdef = tiled.graph.as_graph_def()

    # Move the tile op to the start of the graph so that shapes of its inputs
    # are not available when the shape function runs on import.
    swapped = False
    for i, n in enumerate(gdef.node):
        if n.op == "Tile":
            # Swap tile op to be first in gdef.node
            assert i != 0
            new_node = node_def_pb2.NodeDef()
            new_node.CopyFrom(gdef.node[i])
            gdef.node[i].CopyFrom(gdef.node[0])
            gdef.node[0].CopyFrom(new_node)
            swapped = True
    assert swapped

    tiled_imported, = importer.import_graph_def(
        gdef, return_elements=[tiled.name])
    self.assertEqual(4, tiled_imported.get_shape().ndims)
