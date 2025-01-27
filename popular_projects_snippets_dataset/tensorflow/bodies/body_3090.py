# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/duplicate_method_names_v1.py

x = tf.constant(1.0, shape=(3, 3))
y = tf.constant(1.0, shape=(3, 3))

s = tf.transpose(x)
t = tf.transpose(y)

tensor_info_s = tf.compat.v1.saved_model.utils.build_tensor_info(s)
tensor_info_t = tf.compat.v1.saved_model.utils.build_tensor_info(t)

signature_def = tf.saved_model.signature_def_utils.build_signature_def(
    inputs=None, outputs={'s': tensor_info_s}, method_name='some_function')
signature_def2 = tf.saved_model.signature_def_utils.build_signature_def(
    inputs=None, outputs={'t': tensor_info_t}, method_name='some_function')

# Create two signatures that share the same variable.
exit(({'key': signature_def, 'key2': signature_def2}, None, None))
