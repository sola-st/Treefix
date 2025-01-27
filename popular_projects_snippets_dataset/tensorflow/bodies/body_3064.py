# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/basic_v1.py

x = tf.constant([[1.0], [1.0], [1.0]])
y = tf.compat.v1.get_variable(
    name='y',
    shape=(1, 3),
    initializer=tf.random_normal_initializer(),
    trainable=True)
r = tf.matmul(x, y)

tensor_info_x = tf.compat.v1.saved_model.utils.build_tensor_info(x)
tensor_info_r = tf.compat.v1.saved_model.utils.build_tensor_info(r)

exit(({
    'key': (tf.compat.v1.saved_model.signature_def_utils.build_signature_def(
        inputs={'x': tensor_info_x},
        outputs={'r': tensor_info_r},
        method_name='some_function'))
}, None, None))
