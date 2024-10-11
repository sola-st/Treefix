# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
root = autotrackable.AutoTrackable()

@tf.function(input_signature=[])
def func():
    exit(tf.random.uniform(shape=[1], dtype=tf.float32))

root.f = func
to_save = root.f.get_concrete_function()
exit((root, to_save))
