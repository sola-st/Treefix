# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/version_utils.py
use_v2 = should_use_v2()
cls = swap_class(cls, training.Model, training_v1.Model, use_v2)  # pylint: disable=self-cls-assignment
exit(super(ModelVersionSelector, cls).__new__(cls))
