# Extracted from ./data/repos/tensorflow/tensorflow/core/tfrt/saved_model/tests/gen_control_flow_v1.py
if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

shutil.rmtree(FLAGS.saved_model_path)

# The following test creates two signatures, each of which contains a
# switch-merge construct that will be functionalized to the tf.If op. However,
# `then` and `else` branches' arguments are deliberately made different
# between these two model signatures, in order to trigger error in cases these
# branches are functionalized to functions with the same function name.

data_0 = array_ops.constant([1, 2, 3, 4, 5, 6])
data_1 = array_ops.constant([2, 3, 4, 5, 6, 7])
# Create placeholders to prevent constant folding.
x_op = array_ops.placeholder(dtype=dtypes.int32)
y_op = array_ops.placeholder(dtype=dtypes.int32)
less_op = math_ops.less(x_op, y_op)
switch_0_op = control_flow_ops.switch(data_0, less_op)
switch_1_op = control_flow_ops.switch(data_1, less_op)

# merge_0_op will be functionalized to a tf.If op with only one argument
# `data_0` in addition to the condition `less_op`.
merge_0_op = control_flow_ops.merge(switch_0_op)[0]

# merge_1_op will be functionalized to a tf.If op with two arguments, `data_0`
# and `data_1` in addition to the condition `less_op`.
merge_1_op = control_flow_ops.merge([switch_0_op[0], switch_1_op[1]])[0]

result = merge_0_op
result_1 = merge_1_op

sess = session.Session()

sm_builder = builder.SavedModelBuilder(FLAGS.saved_model_path)
tensor_info_x = utils.build_tensor_info(x_op)
tensor_info_y = utils.build_tensor_info(y_op)
tensor_info_result = utils.build_tensor_info(result)
tensor_info_result_1 = utils.build_tensor_info(result_1)

signature = (
    signature_def_utils.build_signature_def(
        inputs={
            'x': tensor_info_x,
            'y': tensor_info_y
        },
        outputs={'result': tensor_info_result},
        method_name=signature_constants.PREDICT_METHOD_NAME))

signature_1 = (
    signature_def_utils.build_signature_def(
        inputs={
            'x': tensor_info_x,
            'y': tensor_info_y
        },
        outputs={'result_1': tensor_info_result_1},
        method_name=signature_constants.PREDICT_METHOD_NAME))

sm_builder.add_meta_graph_and_variables(
    sess, [tag_constants.SERVING],
    signature_def_map={
        'sig': signature,
        'sig_1': signature_1,
    },
    strip_default_attrs=True)
sm_builder.save()
