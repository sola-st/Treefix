# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/item_test.py
with ops.Graph().as_default() as g:
    a = constant_op.constant(10)
    b = constant_op.constant(20)
    c = a + b  # pylint: disable=unused-variable
    mg = meta_graph.create_meta_graph_def(graph=g)

# The train op isn't specified: this should raise an InvalidArgumentError
# exception.
with self.assertRaises(errors_impl.InvalidArgumentError):
    item.Item(mg)
