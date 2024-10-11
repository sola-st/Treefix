# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/conv_node_name_test.py

def _GetNodeNames(use_xla):
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

xla_names = _GetNodeNames(use_xla=True)
no_xla_names = _GetNodeNames(use_xla=False)

# CPU path creates some additional nodes to handle dilations.
# TODO(b/138804006): Remove this when CPU & GPU support dilations.
filtered_no_xla_names = []
for name in no_xla_names:
    if ("dilation_rate" in name or "filter_shape" in name or "stack" in name):
        continue
    else:
        filtered_no_xla_names.append(name)

self.assertListEqual(xla_names, filtered_no_xla_names)
