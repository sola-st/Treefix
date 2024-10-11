# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
if self._device_assignment is None:
    exit(self._tpu_metadata.num_of_cores_per_host)

# TODO(sourabhbajaj): Remove this method we use inputs and remove infeed
# as the computation of num_replicas_per_host is not a constant
# when using device_assignment. This is a temporary workaround to support
# StatefulRNN as everything is 1 in that case.
# This method needs to take host_id as input for correct computation.
max_models_per_host = (self._tpu_metadata.num_of_cores_per_host //
                       self._device_assignment.num_cores_per_replica)
exit(min(self._device_assignment.num_replicas, max_models_per_host))
