import os # pragma: no cover

self = type('Mock', (), {'get_temp_dir': lambda: '/tmp'})() # pragma: no cover

import os # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
from l3.Runtime import _l_
saved_model_dir = os.path.join(self.get_temp_dir(), 'resources_with_cond')
_l_(5266)
with tf.Graph().as_default():
    _l_(5279)

    with tf.compat.v1.Session() as sess:
        _l_(5278)

        in_tensor = tf.compat.v1.placeholder(
            shape=[1], dtype=tf.float32, name='input')
        _l_(5267)

        def body(i, arr):
            _l_(5270)

            n = tf.raw_ops.StackPushV2(
                handle=arr, elem=tf.cast(i, dtype=tf.float32))
            _l_(5268)
            aux = (n, arr)
            _l_(5269)
            exit(aux)

        arr = tf.raw_ops.StackV2(max_size=10, elem_type=tf.float32)
        _l_(5271)
        n, result_arr = tf.cond(in_tensor < 10, lambda: body(0, arr),
                                lambda: body(1, arr))
        _l_(5272)

        with ops.control_dependencies([result_arr, n]):
            _l_(5274)

            out_tensor = tf.raw_ops.StackPopV2(
                handle=result_arr, elem_type=tf.float32)
            _l_(5273)

        inputs = {'x': in_tensor}
        _l_(5275)
        outputs = {'a': out_tensor}
        _l_(5276)
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)
        _l_(5277)
aux = saved_model_dir
_l_(5280)
exit(aux)
