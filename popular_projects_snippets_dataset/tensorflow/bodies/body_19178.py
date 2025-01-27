# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Creates tensors for SparseFeatures and RaggedFeatures.

  Constructs new dict based on `tensor_dict`.

  For each key in `features` whose value is a `SparseFeature`:

    * Looks up that SparseFeature's value_key and index_keys in tensor_dict.
    * Uses those tensors to construct a single SparseTensor.
    * Stores that SparseTensor in the output dict under the same key.

  For each key in `features` whose value is a `RaggedFeature`:

    * Looks up that RaggedFeature's value_key and partition keys in tensor_dict.
    * Uses those tensors to construct a single RaggedTensor.
    * Stores that RaggedTensor in the output dict under the same key.

  For any other key in `features`:

    * Copies that key and its value from tensor_dict to the output dictionary.

  Args:
    features: A `dict` mapping feature keys to `SparseFeature` or
      `RaggedFeature` values.  Values of other types will be ignored.
    tensor_dict: A `dict` mapping feature keys to `Tensor`, `SparseTensor`, and
      `RaggedTensor` values.  Expected to contain keys of the `SparseFeature`s'
      `index_key`s and `value_key`s and mapping them to `SparseTensor`s.

  Returns:
    A `dict` mapping feature keys to `Tensor`, `SparseTensor`, and
    `RaggedTensor` values. Similar to `tensor_dict` except each `SparseFeature`
    in `features` results in a single `SparseTensor`; and each `RaggedFeature`
    in `features` results in a single `RaggedTensor`.
  """
tensor_dict = dict(tensor_dict)  # Do not modify argument passed in.
updates = {}
for key in sorted(features.keys()):
    feature = features[key]
    if isinstance(feature, SparseFeature):
        # Construct SparseTensors for SparseFeatures
        if isinstance(feature.index_key, str):
            sp_ids = tensor_dict[feature.index_key]
        else:
            sp_ids = [tensor_dict[index_key] for index_key in feature.index_key]
        sp_values = tensor_dict[feature.value_key]
        updates[key] = sparse_ops.sparse_merge(
            sp_ids,
            sp_values,
            vocab_size=feature.size,
            already_sorted=feature.already_sorted)
    elif isinstance(feature, RaggedFeature):
        # Construct RaggedTensors for RaggedFeatures.
        value_key = key if feature.value_key is None else feature.value_key
        rt = tensor_dict[value_key]
        if isinstance(rt, ragged_tensor.RaggedTensor):
            # We processed a batch of tf.Example or tf.SequenceExample, or single
            # tf.SequenceExample.
            if rt.ragged_rank > 1:
                # We're processing a batch of SequenceExample, and we effectively have
                # two batch dimensions.  Cllapse those batch dimensions here, and
                # restore them below (using outer_splits).
                outer_splits = rt.row_splits
                rt = rt.values
            else:
                outer_splits = None
            for partition in reversed(feature.partitions):
                rt = _add_batched_ragged_partition(rt, partition, tensor_dict,
                                                   key, feature.validate,
                                                   outer_splits)
            if outer_splits is not None:
                rt = ragged_tensor.RaggedTensor.from_row_splits(
                    rt, outer_splits, validate=feature.validate)
        else:
            # We processed a single tf.Example.
            for partition in reversed(feature.partitions):
                rt = _add_ragged_partition(rt, partition, tensor_dict,
                                           feature.row_splits_dtype, feature.validate)
        updates[key] = rt

  # Process updates after all composite tensors have been constructed (in case
  # multiple features use the same value_key, and one uses that key as its
  # feature key).
tensor_dict.update(updates)

# Remove tensors from dictionary that were only used to construct
# tensors for SparseFeature or RaggedTensor.
for key in set(tensor_dict) - set(features):
    del tensor_dict[key]
exit(tensor_dict)
