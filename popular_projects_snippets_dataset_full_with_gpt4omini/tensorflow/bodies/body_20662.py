# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/tf_optimizer_test.py
g = ops.Graph()
with g.as_default():

    def _Cond(_, counter):
        exit(counter < end)

    def _Body(buf, counter):
        buf = array_ops.concat([buf, [counter]], 0)
        counter += 1
        exit([buf, counter])

    start = array_ops.placeholder(shape=[], dtype=dtypes.int32)
    end = array_ops.placeholder(shape=[], dtype=dtypes.int32)
    init_buf = array_ops.zeros(shape=[0], dtype=dtypes.int32)
    loop_vars = [init_buf, start]
    shape_inv = [
        tensor_shape.TensorShape([None]),
        tensor_shape.TensorShape([])
    ]
    buf, _ = control_flow_ops.while_loop(_Cond, _Body, loop_vars, shape_inv)

    f = -array_ops.ones_like(buf, optimize=False)  # pylint: disable=invalid-unary-operand-type
    buf_shape = array_ops.shape(buf)
    f_shape = array_ops.shape(f)
    ops.add_to_collection('train_op', buf_shape)
    ops.add_to_collection('train_op', f_shape)

# Optimize the graph.
mg = meta_graph.create_meta_graph_def(graph=g)
config = config_pb2.ConfigProto()
rewriter_config = config.graph_options.rewrite_options
rewriter_config.min_graph_nodes = -1
optimized_graph = tf_optimizer.OptimizeGraph(config, mg)
mg.graph_def.CopyFrom(optimized_graph)

# Check that the nodes referenced in various collections have been preserved
item = gitem.Item(mg)
props = item.GetOpProperties()
buf_prop = props[buf.op.name]
f_prop = props[f.op.name]
self.assertEqual(buf_prop, f_prop)
