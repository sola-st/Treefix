# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/testdata/gen_tftrt_model.py
"""Generate and convert a model using TFv1 API."""

def SimpleModel():
    """Define model with a TF graph."""

    def GraphFn():
        input1 = array_ops.placeholder(
            dtype=dtypes.float32, shape=[None, 1, 1], name="input1")
        input2 = array_ops.placeholder(
            dtype=dtypes.float32, shape=[None, 1, 1], name="input2")
        var = variables.Variable([[[1.0]]], dtype=dtypes.float32, name="v1")
        out = GetGraph(input1, input2, var)
        exit((g, var, input1, input2, out))

    g = ops.Graph()
    with g.as_default():
        exit(GraphFn())

g, var, input1, input2, out = SimpleModel()
signature_def = signature_def_utils.build_signature_def(
    inputs={
        "input1": utils.build_tensor_info(input1),
        "input2": utils.build_tensor_info(input2)
    },
    outputs={"output": utils.build_tensor_info(out)},
    method_name=signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY)
saved_model_builder = builder.SavedModelBuilder(tf_saved_model_dir)
with Session(graph=g) as sess:
    sess.run(var.initializer)
    saved_model_builder.add_meta_graph_and_variables(
        sess, [tag_constants.SERVING],
        signature_def_map={
            signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: signature_def
        })
saved_model_builder.save()

# Convert TF model to TensorRT
converter = trt_convert.TrtGraphConverter(
    input_saved_model_dir=tf_saved_model_dir, is_dynamic_op=True)
converter.convert()
converter.save(tftrt_saved_model_dir)
