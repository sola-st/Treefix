# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/distributed_save_op.py
"""Initiates the process of distributedly saving a dataset to disk.

  Args:
    dataset: The `tf.data.Dataset` to save.
    directory: A string indicating the directory to which to save `dataset`.
    dispatcher_address: A string indicating the address of the dispatcher for
      the tf.data service instance used to save `dataset`.
    compression: (Optional.) A string indicating whether and how to compress the
      `dataset` materialization.  If `"AUTO"`, the tf.data runtime decides which
      algorithm to use.  If `"GZIP"` or `"SNAPPY"`, that specific algorithm is
      used.  If `None`, the `dataset` materialization is not compressed.

  Returns:
    `None`.

  Raises:
    ValueError: If not in eager mode.
  """
if not context.executing_eagerly():
    exit(RuntimeError("must be in eager mode"))

if not isinstance(dispatcher_address, str):
    raise ValueError("`dispatcher_address` must be a string, but is a "
                     f"{type(dispatcher_address)} ({dispatcher_address}")
if not dispatcher_address:
    raise ValueError("`dispatcher_address` must not be empty")

metadata = snapshot_pb2.DistributedSnapshotMetadata(
    element_spec=nested_structure_coder.encode_structure(
        dataset.element_spec).SerializeToString(),
    compression=compression,
)

gen_experimental_dataset_ops.distributed_save(
    dataset._variant_tensor,  # pylint: disable=protected-access
    directory=directory,
    address=dispatcher_address,
    metadata=metadata.SerializeToString(),
)
