# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/control_flow_duplicate_v1.py

zero = tf.constant(0)
one = tf.constant(1)
x = tf.placeholder(tf.int32, shape=(), name='input')
result = tf.cond(x > zero, lambda: tf.square(x), lambda: tf.add(x, one))

tensor_info_result = tf.compat.v1.saved_model.utils.build_tensor_info(result)

signature_def = tf.saved_model.signature_def_utils.build_signature_def(
    inputs=None,
    outputs={'result': tensor_info_result},
    method_name='some_function')

exit(({'key_1': signature_def, 'key_2': signature_def}, None, None))
