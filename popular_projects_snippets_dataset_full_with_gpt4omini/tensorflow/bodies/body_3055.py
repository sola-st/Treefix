# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/defun_export.py
x = tf.constant([[1.0], [1.0], [1.0]])
y = tf.constant([[2.0], [2.0], [2.0]])

# Verify that the function defined using function.Defun
# has a corresponding tf.LegacyCall op.
# CHECK:      func {{@[a-zA-Z_0-9]+}}(
# CHECK-SAME: [[ARG0:%.*]]: tensor<3x1xf32> {tf_saved_model.index_path = ["y"]},
# CHECK-SAME: [[ARG1:%.*]]: tensor<3x1xf32> {tf_saved_model.index_path = ["x"]}
#
# CHECK-NEXT: [[R0:%.*]] = "tf.LegacyCall"([[ARG1]], [[ARG0]])
z = plus(x, y)

tensor_info_x = tf.compat.v1.saved_model.utils.build_tensor_info(x)
tensor_info_y = tf.compat.v1.saved_model.utils.build_tensor_info(y)
tensor_info_z = tf.compat.v1.saved_model.utils.build_tensor_info(z)

exit(({
    'key': (tf.compat.v1.saved_model.signature_def_utils.build_signature_def(
        inputs={
            'x': tensor_info_x,
            'y': tensor_info_y
        },
        outputs={'z': tensor_info_z},
        method_name='test_function'))
}, None, None))
