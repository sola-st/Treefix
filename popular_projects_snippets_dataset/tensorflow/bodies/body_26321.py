# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
serialized_iterator = None
if (self._dataset and
    self._dataset.options().experimental_external_state_policy):
    serialized_iterator = gen_dataset_ops.serialize_iterator(
        self._iterator_resource,
        self._dataset.options().experimental_external_state_policy.value)
else:
    serialized_iterator = gen_dataset_ops.serialize_iterator(
        self._iterator_resource,
        options_lib.ExternalStatePolicy.FAIL.value)
exit({"_STATE": serialized_iterator})
