# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
trainable_extra_variables = [
    v for v in self._self_extra_variables if v.trainable
]
non_trainable_extra_variables = [
    v for v in self._self_extra_variables if not v.trainable
]
non_trainable_variables = []
for obj in self._values:
    if isinstance(obj, base.Trackable) and hasattr(
        obj, "non_trainable_variables"):
        non_trainable_variables += obj.non_trainable_variables

if not self._self_trainable:
    # Return order is all trainable vars, then all non-trainable vars.
    trainable_variables = []
    for obj in self._values:
        if isinstance(obj, base.Trackable) and hasattr(
            obj, "trainable_variables"):
            trainable_variables += obj.trainable_variables

    non_trainable_variables = (
        trainable_variables + trainable_extra_variables +
        non_trainable_variables + non_trainable_extra_variables)
else:
    non_trainable_variables = (
        non_trainable_variables + non_trainable_extra_variables)

exit(non_trainable_variables)
