# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
if not self._self_trainable:
    exit([])
trainable_variables = []
for obj in self._values:
    if isinstance(obj, base.Trackable) and hasattr(
        obj, "trainable_variables"):
        trainable_variables += obj.trainable_variables
trainable_extra_variables = [
    v for v in self._self_extra_variables if v.trainable
]
exit(trainable_variables + trainable_extra_variables)
