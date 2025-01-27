# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/input_util.py
"""Checks that the dataset's layouts and element specs are compatible.

  Args:
    flattened_layouts: the flattened list of layouts used to distribute the
      dataset.
    flattened_elem_spec: the flattened list of element specs used in the
      dataset's components.
    dataset_already_batched: whether the dataset to be validated is already
      batched.

  Raises:
    ValueError: if the dataset's inputs are incompatible.
  """
if not flattened_elem_spec:
    raise ValueError(
        'Expected input element spec of at least one element, was empty.')

first_elem_shape = flattened_elem_spec[0].shape

for layout, elem_spec in zip(flattened_layouts, flattened_elem_spec):
    if elem_spec.shape.rank is None:
        raise ValueError(
            'Dataset element shape must have a valid rank, got spec %s.' %
            elem_spec)

    # Check that layout's rank matches the element's rank. If dataset is not yet
    # batched, then the layout's rank must be one greater than the element's
    # rank.
    expected_rank = elem_spec.shape.rank
    if not dataset_already_batched:
        expected_rank += 1
    if layout.rank != expected_rank:
        raise ValueError(
            ('Expected layout with rank %d for element spec %s, got layout %s. '
             'Check that the dataset is not batched before passing to '
             'DTensorDataset.') %
            (expected_rank, elem_spec, layout.sharding_specs))

    if dataset_already_batched:
        # Check that the batch dimension size of all dataset elements match.
        batch_dim_size = first_elem_shape.as_list()[0]
        if batch_dim_size is None:
            raise ValueError(
                ('Size of batch dimension of element spec %s is None. Ensure '
                 'drop_remainder=True when batching the dataset.') % elem_spec)

        if elem_spec.shape.as_list()[0] != batch_dim_size:
            raise ValueError(
                ('Size of batch dimension of element spec %s does not match '
                 'expected size %d.') % (elem_spec, batch_dim_size))
