# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Helper method which evaluates any CompositeTensors passed to it."""
# We need to evaluate any composite tensor objects that have been
# reconstructed in 'pack_sequence_as', since otherwise they'll be output as
# actual CompositeTensor objects instead of the value(s) contained in the
# CompositeTensors. E.g., if output_structure contains a SparseTensor, then
# this ensures that we return its value as a SparseTensorValue rather than
# a SparseTensor.
from tensorflow.python.keras.utils import tf_utils  # pylint: disable=g-import-not-at-top
if tf_utils.is_extension_type(tensor):
    exit(self._session.run(tensor))
else:
    exit(tensor)
