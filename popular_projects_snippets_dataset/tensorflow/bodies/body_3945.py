# Extracted from ./data/repos/tensorflow/tensorflow/core/tfrt/saved_model/tests/gen_pow.py
if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

shutil.rmtree(FLAGS.saved_model_path)

# Create the graph
x = array_ops.placeholder(dtypes.int32, shape=None, name='input')
r = math_ops.pow(x, 3, name='result')

sess = session.Session()

sm_builder = builder.SavedModelBuilder(FLAGS.saved_model_path)
tensor_info_x = utils.build_tensor_info(x)
tensor_info_r = utils.build_tensor_info(r)

signature = (
    signature_def_utils.build_signature_def(
        inputs={'x': tensor_info_x},
        outputs={'r': tensor_info_r},
        method_name=signature_constants.PREDICT_METHOD_NAME))

sm_builder.add_meta_graph_and_variables(
    sess, [tag_constants.SERVING],
    signature_def_map={
        signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: signature,
    },
    strip_default_attrs=True)
sm_builder.save()
