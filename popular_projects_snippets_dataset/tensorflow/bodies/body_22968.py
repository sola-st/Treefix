# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
saved_model_builder = builder.SavedModelBuilder(output_dir)
graph = ops.Graph()
with session.Session(graph=graph) as sess:
    with graph.device('/GPU:0'):
        x = array_ops.placeholder(
            shape=(None, 28, 28, 1), dtype=dtypes.float32, name=INPUT_NODE_NAME)
        self._BuildGraph(x)
    self._LoadWeights(model_dir, sess)
    input_tensor = graph.get_tensor_by_name(INPUT_NODE_NAME + ':0')
    output = graph.get_tensor_by_name(OUTPUT_NODE_NAME + ':0')
    signature_def = signature_def_utils.build_signature_def(
        inputs={'input': saved_model_utils.build_tensor_info(input_tensor)},
        outputs={'output': saved_model_utils.build_tensor_info(output)},
        method_name=signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY)
    saved_model_builder.add_meta_graph_and_variables(
        sess, [tag_constants.SERVING],
        signature_def_map={
            signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
                signature_def
        })
saved_model_builder.save()
