# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert_test.py
saved_model_dir = self._getFilepath('model')
with ops.Graph().as_default():
    with session.Session() as sess:
        in_tensor = array_ops.placeholder(
            shape=[1, 16, 16, 3], dtype=dtypes.float32, name='inputB')
        out_tensor = in_tensor + in_tensor
        inputs = {'x': in_tensor}
        outputs = {'z': out_tensor}
        saved_model.simple_save(sess, saved_model_dir, inputs, outputs)

flags_str = '--saved_model_dir={}'.format(saved_model_dir)
self._run(flags_str, should_succeed=True)
