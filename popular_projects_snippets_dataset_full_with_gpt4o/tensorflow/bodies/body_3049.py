# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/multi_arguments_results_v1.py

x = tf.constant(1.0, shape=(5, 3))
y = tf.constant(1.0, shape=(3, 5))

s = tf.matmul(x, y)
t = tf.matmul(y, x)
[t, s] = array_ops.identity_n([t, s])

tensor_info_x = tf.compat.v1.saved_model.utils.build_tensor_info(x)
tensor_info_y = tf.compat.v1.saved_model.utils.build_tensor_info(y)
tensor_info_s = tf.compat.v1.saved_model.utils.build_tensor_info(s)
tensor_info_t = tf.compat.v1.saved_model.utils.build_tensor_info(t)

exit(({
    'key': (tf.compat.v1.saved_model.signature_def_utils.build_signature_def(
        inputs={
            'x': tensor_info_x,
            'y': tensor_info_y
        },
        outputs={
            's': tensor_info_s,
            't': tensor_info_t
        },
        method_name='some_function')),
    'key2': (tf.compat.v1.saved_model.signature_def_utils.build_signature_def(
        inputs={
            'a': tensor_info_y,
            'b': tensor_info_x,
        },
        outputs={
            'c': tensor_info_t,
            'd': tensor_info_s,
        },
        method_name='reverse_arguments'))
}, None, None))
