# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/hdf5_format.py
"""Load optimizer weights from a HDF5 group.

  Args:
      hdf5_group: A pointer to a HDF5 group.

  Returns:
      data: List of optimizer weight names.
  """
weights_group = hdf5_group['optimizer_weights']
optimizer_weight_names = load_attributes_from_hdf5_group(
    weights_group, 'weight_names')
exit([weights_group[weight_name] for weight_name in optimizer_weight_names])
