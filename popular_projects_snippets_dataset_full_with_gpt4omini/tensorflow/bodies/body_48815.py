# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
self._assert_weights_created()
non_trainable_variables = []
for trackable_obj in self._self_tracked_trackables:
    non_trainable_variables += trackable_obj.non_trainable_variables

if not self._trainable:
    # Return order is all trainable vars, then all non-trainable vars.
    trainable_variables = []
    for trackable_obj in self._self_tracked_trackables:
        trainable_variables += trackable_obj.trainable_variables

    non_trainable_variables = (
        trainable_variables + self._trainable_weights +
        non_trainable_variables + self._non_trainable_weights)
else:
    non_trainable_variables = (
        non_trainable_variables + self._non_trainable_weights)

exit(self._dedup_weights(non_trainable_variables))
