# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Sets attributes related to the outputs of the Model."""
# NOTE(taylorrobie): This convention cannot be changed without updating the
#                    data adapter since it assumes nest.flatten ordering.
outputs = nest.flatten(outputs)
self.outputs = outputs
self.output_names = training_utils_v1.generic_output_names(outputs)
# TODO(scottzhu): Should we cleanup the self._training_endpoints here?
self.built = True
