# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/multi_variables_v1.py

x = tf.compat.v1.get_variable(
    name='x',
    shape=(5, 3),
    initializer=tf.random_normal_initializer(),
    trainable=True)
y = tf.compat.v1.get_variable(
    name='y',
    shape=(3, 5),
    initializer=tf.random_normal_initializer(),
    trainable=True)
z = tf.matmul(x, y)
tensor_info_z = tf.compat.v1.saved_model.utils.build_tensor_info(z)

exit(({
    'key': (tf.compat.v1.saved_model.signature_def_utils.build_signature_def(
        inputs=None,
        outputs={'z': tensor_info_z},
        method_name='some_function'))
}, None, None))
