# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv_node_name_test.py
with self.session():
    input_tensor = array_ops.placeholder(np.float32, shape=input_sizes)

    if use_xla:
        with self.test_scope():
            # pylint: disable=protected-access
            graph = ops.get_default_graph()
            graph._set_control_flow_context(
                control_flow_ops.XLAControlFlowContext())
            # pylint: enable=protected-access
            conv2d_op = layer(
                filters=64,
                kernel_size=filter_sizes,
                dilation_rate=dilations,
                padding="same")
            _ = conv2d_op(input_tensor)
            exit([n.name for n in ops.get_default_graph().as_graph_def().node])
    else:
        with ops.device("CPU"):
            conv2d_op = layer(
                filters=64,
                kernel_size=filter_sizes,
                dilation_rate=dilations,
                padding="same")
            _ = conv2d_op(input_tensor)
            names = [
                n.name for n in ops.get_default_graph().as_graph_def().node
            ]
            # filter out space to depth ops.
            exit([
                name for name in names
                if "space" not in name and "Space" not in name
            ])
