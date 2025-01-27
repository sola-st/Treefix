# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
"""Registers a dataset with the tf.data service.

  This transformation is similar to `register_dataset`, but supports additional
  parameters which we do not yet want to add to the public Python API.

  Args:
    service: A string or a tuple indicating how to connect to the tf.data
      service. If it's a string, it should be in the format
      `[<protocol>://]<address>`, where `<address>` identifies the dispatcher
        address and `<protocol>` can optionally be used to override the default
        protocol to use. If it's a tuple, it should be (protocol, address).
    dataset: A `tf.data.Dataset` to register with the tf.data service.
    compression: How to compress the dataset's elements before transferring them
      over the network. "AUTO" leaves the decision of how to compress up to the
      tf.data service runtime. `None` indicates not to compress.
    dataset_id: (Optional.) By default, tf.data service generates a unique
      (string) ID for each registered dataset. If a `dataset_id` is provided, it
      will use the specified ID. If a dataset with a matching ID already exists,
      no new dataset is registered. This is useful if multiple training jobs
      want to (re)use the same dataset for training. In this case, they can
      register the dataset with the same dataset ID.

  Returns:
    A scalar string tensor representing the dataset ID.
  """
_validate_compression(compression)
if isinstance(service, tuple):
    protocol, address = service
else:
    protocol, address = _parse_service(service)
external_state_policy = dataset.options().experimental_external_state_policy
if external_state_policy is None:
    external_state_policy = ExternalStatePolicy.WARN

encoded_spec = None
if context.executing_eagerly():
    encoded_spec = nested_structure_coder.encode_structure(
        dataset.element_spec).SerializeToString()

if compression == COMPRESSION_AUTO:
    dataset = dataset.map(
        lambda *x: compression_ops.compress(x),
        num_parallel_calls=dataset_ops.AUTOTUNE)
dataset = dataset.prefetch(dataset_ops.AUTOTUNE)
dataset = dataset._apply_debug_options()  # pylint: disable=protected-access

metadata = data_service_pb2.DataServiceMetadata(
    element_spec=encoded_spec,
    compression=_get_compression_proto(compression))

exit(gen_experimental_dataset_ops.register_dataset_v2(
    dataset._variant_tensor,  # pylint: disable=protected-access
    address=address,
    protocol=protocol,
    external_state_policy=external_state_policy.value,
    requested_dataset_id=dataset_id,
    metadata=metadata.SerializeToString()))
