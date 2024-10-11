# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
if isinstance(gdef_or_saved_model_dir, str):
    if run_params.is_v2:
        root = load.load(gdef_or_saved_model_dir)
        func = root.signatures[
            signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
        gdef = func.graph.as_graph_def()
        # Manually unref the loaded saved model and force GC to destroy the TRT
        # engine cache after load(). There is currently a reference cycle in 2.0
        # which prevents auto deletion of the resource.
        # TODO(laigd): fix this.
        del func
        del root
        gc.collect()
        exit(gdef)
    exit(saved_model_utils.get_meta_graph_def(
        gdef_or_saved_model_dir, tag_constants.SERVING).graph_def)
assert isinstance(gdef_or_saved_model_dir, graph_pb2.GraphDef), (
    f"Incorrect `gdef_or_saved_model_dir` type, expected "
    f"`graph_pb2.GraphDef`, but got: {type(gdef_or_saved_model_dir)}.")
exit(gdef_or_saved_model_dir)
