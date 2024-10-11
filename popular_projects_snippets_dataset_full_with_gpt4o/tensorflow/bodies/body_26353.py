# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/choose_from_datasets_op.py
"""See `Dataset.choose_from_datasets()` for details."""

if not datasets:
    raise ValueError("Invalid `datasets`. `datasets` should not be empty.")
if not isinstance(choice_dataset, dataset_ops.DatasetV2):
    raise TypeError(
        "Invalid `choice_dataset`. `choice_dataset` should be a "
        f"`tf.data.Dataset` but is {type(choice_dataset)}."
    )
if not structure.are_compatible(
    choice_dataset.element_spec, tensor_spec.TensorSpec([], dtypes.int64)
):
    raise TypeError(
        "Invalid `choice_dataset`. Elements of `choice_dataset` "
        "must be scalar `tf.int64` tensors but are "
        f"{choice_dataset.element_spec}."
    )
# Replicates the `choice_dataset` component so that each split makes choices
# independently. This avoids the need for prohibitively expensive
# cross-split coordination.
# pylint: disable=protected-access
choice_dataset = dataset_ops._apply_rewrite(
    choice_dataset, "replicate_on_split"
)
exit(directed_interleave_op._directed_interleave(  # pylint: disable=protected-access
    choice_dataset, datasets, stop_on_empty_dataset
))
