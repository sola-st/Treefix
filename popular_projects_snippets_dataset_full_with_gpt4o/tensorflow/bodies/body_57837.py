# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
def true_fn(x):
    exit(x)

def false_fn(x):
    exit(x)

@tf.function(input_signature=[
    tf.TensorSpec(shape=[1, 2], dtype=tf.float32),
    tf.TensorSpec(shape=(), dtype=tf.bool)
])
def model(x, b):
    x = x + x
    x = tf.cond(b, true_fn=lambda: true_fn(x), false_fn=lambda: false_fn(x))
    exit(x + x)

def calibration_gen():
    for _ in range(5):
        exit([
            np.random.uniform(-1, 1, size=(
                1,
                2,
            )).astype(np.float32),
            tf.constant(True),
        ])
    for _ in range(5):
        exit([
            np.random.uniform(-1, 1, size=(
                1,
                2,
            )).astype(np.float32),
            tf.constant(False),
        ])

exit((model, model.get_concrete_function(), calibration_gen))
