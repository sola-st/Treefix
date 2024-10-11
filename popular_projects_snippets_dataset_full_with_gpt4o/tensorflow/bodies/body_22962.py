# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
"""Gets the frozen mnist GraphDef.

    Args:
      use_trt: whether use TF-TRT to convert the graph.
      max_batch_size: the max batch size to apply during TF-TRT conversion.
      model_dir: the model directory to load the checkpoints.

    Returns:
      The frozen mnist GraphDef.
    """
graph = ops.Graph()
with self.session(graph=graph) as sess:
    with graph.device('/GPU:0'):
        x = array_ops.placeholder(
            shape=(None, 28, 28, 1), dtype=dtypes.float32, name=INPUT_NODE_NAME)
        self._BuildGraph(x)
    self._LoadWeights(model_dir, sess)
    # Freeze
    graph_def = graph_util.convert_variables_to_constants(
        sess, sess.graph_def, output_node_names=[OUTPUT_NODE_NAME])
# Convert with TF-TRT
if use_trt:
    logging.info('Number of nodes before TF-TRT conversion: %d',
                 len(graph_def.node))
    converter = trt_convert.TrtGraphConverter(
        input_graph_def=graph_def,
        nodes_denylist=[OUTPUT_NODE_NAME],
        max_batch_size=max_batch_size,
        precision_mode='INT8',
        max_workspace_size_bytes=(
            trt_convert.DEFAULT_TRT_MAX_WORKSPACE_SIZE_BYTES),
        minimum_segment_size=2,
        use_calibration=False)
    graph_def = converter.convert()
    logging.info('Number of nodes after TF-TRT conversion: %d',
                 len(graph_def.node))
    num_engines = len(
        [1 for n in graph_def.node if str(n.op) == 'TRTEngineOp'])
    self.assertEqual(1, num_engines)
exit(graph_def)
