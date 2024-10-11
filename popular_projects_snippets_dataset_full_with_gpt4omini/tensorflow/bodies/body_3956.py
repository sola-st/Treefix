# Extracted from ./data/repos/tensorflow/tensorflow/core/tfrt/saved_model/tests/gen_sparse_tensor_input.py
if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

shutil.rmtree(FLAGS.saved_model_path)

# Create the graph
x = array_ops.sparse_placeholder(dtype=dtypes.int32, shape=None, name='input')
r = sparse_ops.sparse_reduce_sum(x)

x1 = array_ops.placeholder(dtype=dtypes.int32, shape=(1, 3), name='input1')
r1 = math_ops.add(x1, 1)

sess = session.Session()

sm_builder = builder.SavedModelBuilder(FLAGS.saved_model_path)

tensor_info_x = utils.build_tensor_info(x)
tensor_info_r = utils.build_tensor_info(r)

tensor_info_x1 = utils.build_tensor_info(x1)
tensor_info_r1 = utils.build_tensor_info(r1)

sparse_signature = (
    signature_def_utils.build_signature_def(
        inputs={'x': tensor_info_x},
        outputs={'r': tensor_info_r},
        method_name=signature_constants.PREDICT_METHOD_NAME))

dense_signature = (
    signature_def_utils.build_signature_def(
        inputs={'x1': tensor_info_x1},
        outputs={'r1': tensor_info_r1},
        method_name=signature_constants.PREDICT_METHOD_NAME))

sm_builder.add_meta_graph_and_variables(
    sess, [tag_constants.SERVING],
    signature_def_map={
        'sparse': sparse_signature,
        'dense': dense_signature,
    },
    strip_default_attrs=True)
sm_builder.save()
