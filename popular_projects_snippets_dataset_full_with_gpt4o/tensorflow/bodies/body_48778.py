# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
self.train_function = None
self.test_function = None
self.predict_function = None
# Used to cache the `tf.function`'ed `train_function` to be logged in
# TensorBoard, since the original `train_function` is not necessarily
# a `tf.function` (e.g., with ParameterServerStrategy, the `train_function`
# is a scheduling of the actual training function to a remote worker).
self.train_tf_function = None

# Used to cache `trainable` attr of `Layer`s for `fit`.
self._compiled_trainable_state = self._get_trainable_state()
