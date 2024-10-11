# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/control_flow_upgrade_legacy_v1.py
data = tf.constant([1, 2, 3, 4, 5, 6])
# Create placeholders to prevent constant folding.
x_op = tf.placeholder(dtype=tf.int32)
y_op = tf.placeholder(dtype=tf.int32)
less_op = tf.less(x_op, y_op)
switch_op = control_flow_ops.switch(data, less_op)
merge_op = control_flow_ops.merge(switch_op)[0]
result = tf.transpose(merge_op)

tensor_info_result = tf.compat.v1.saved_model.utils.build_tensor_info(result)

signature_def = tf.saved_model.signature_def_utils.build_signature_def(
    inputs=None,
    outputs={'result': tensor_info_result},
    method_name='some_function')

exit(({'key': signature_def}, None, None))
