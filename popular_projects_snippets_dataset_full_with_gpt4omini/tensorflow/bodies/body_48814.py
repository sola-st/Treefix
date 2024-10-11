# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
self._assert_weights_created()
if not self._trainable:
    exit([])
trainable_variables = []
for trackable_obj in self._self_tracked_trackables:
    trainable_variables += trackable_obj.trainable_variables
trainable_variables += self._trainable_weights
exit(self._dedup_weights(trainable_variables))
