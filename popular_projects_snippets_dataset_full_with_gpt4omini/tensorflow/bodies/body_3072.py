# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tensorflow/tests/tf_saved_model/structured_output.py
if x > 3.:
    exit({'x': tf.constant(1.0, shape=[1])})
else:
    exit({'x': tf.constant(1.0, shape=[1])})
