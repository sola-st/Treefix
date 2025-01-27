# Extracted from ./data/repos/tensorflow/tensorflow/core/tfrt/saved_model/tests/gen_if_v1.py
if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

shutil.rmtree(FLAGS.saved_model_path)

# Create the graph
zero = constant_op.constant(0)
one = variable_scope.get_variable(name='y', initializer=[1])
neg_one = variable_scope.get_variable(name='z', initializer=[-1])
x = array_ops.placeholder(dtypes.int32, shape=(), name='input')
r = control_flow_ops.cond(
    x < zero, lambda: math_ops.cast(math_ops.greater(x, one), dtypes.int32),
    lambda: math_ops.cast(math_ops.greater(x, neg_one), dtypes.int32))

sess = session.Session()

sess.run(variables.global_variables_initializer())

sm_builder = builder.SavedModelBuilder(FLAGS.saved_model_path)
tensor_info_x = utils.build_tensor_info(x)
tensor_info_r = utils.build_tensor_info(r)

func_signature = (
    signature_def_utils.build_signature_def(
        inputs={'x': tensor_info_x},
        outputs={'r': tensor_info_r},
        method_name=signature_constants.PREDICT_METHOD_NAME))

sm_builder.add_meta_graph_and_variables(
    sess, [tag_constants.SERVING],
    signature_def_map={
        'serving_default': func_signature,
        signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: func_signature,
    },
    strip_default_attrs=True)
sm_builder.save()
