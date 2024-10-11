# Extracted from ./data/repos/tensorflow/tensorflow/core/tfrt/saved_model/tests/gen_ref_type_tensor_input.py
if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

shutil.rmtree(FLAGS.saved_model_path)

# Create the graph
# 'x' is a read-only Reference Variable in this test case, which will be
# converted to Resource Variable in the MLIR lowering pass.
x = variable_scope.get_variable(name='x', initializer=[[1], [2], [3]])
r = math_ops.add(x, 1)

x1 = array_ops.placeholder(dtype=dtypes.int32, shape=(1, 3), name='input1')
r1 = math_ops.add(x1, 1)

sess = session.Session()

sess.run(variables.global_variables_initializer())

sm_builder = builder.SavedModelBuilder(FLAGS.saved_model_path)

tensor_info_x = utils.build_tensor_info(x)
tensor_info_r = utils.build_tensor_info(r)

tensor_info_x1 = utils.build_tensor_info(x1)
tensor_info_r1 = utils.build_tensor_info(r1)

ref_signature = (
    signature_def_utils.build_signature_def(
        inputs={'x': tensor_info_x},
        outputs={'r': tensor_info_r},
        method_name=signature_constants.PREDICT_METHOD_NAME))

non_ref_signature = (
    signature_def_utils.build_signature_def(
        inputs={'x1': tensor_info_x1},
        outputs={'r1': tensor_info_r1},
        method_name=signature_constants.PREDICT_METHOD_NAME))

sm_builder.add_meta_graph_and_variables(
    sess, [tag_constants.SERVING],
    signature_def_map={
        'ref': ref_signature,
        'non_ref': non_ref_signature,
    },
    strip_default_attrs=True)
sm_builder.save()
