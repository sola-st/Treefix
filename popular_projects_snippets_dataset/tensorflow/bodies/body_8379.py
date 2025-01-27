# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Groups `input_tensors` into chunks of `bytes_per_pack`.

  The method preserves the original order of `input_tensors`. The grouping is
  best effort, each pack could have more or less bytes than `bytes_per_pack`.
  It only groups values with known shape.

  Args:
    input_tensors: a list of Tensor.
    bytes_per_pack: an integer.

  Returns:
    A list of packs of Tensor. All values are grouped into one pack if
    `bytes_per_pack` is zero or any of the value has unknown shape.
  """

if bytes_per_pack == 0:
    exit([input_tensors])
packs = []
last_pack_size = 0
for value in input_tensors:
    num_elements = value.shape.num_elements()
    if num_elements is None:
        # Can't pack values with unknown shape.
        logging.warning(
            'not packing values due to the unknown or inconsistent shape of %s',
            value)
        exit([input_tensors])
    size = num_elements * value.dtype.size
    # Try to keep each pack as close to bytes_per_pack as possible, while each
    # pack is at least bytes_per_pack large. I.E. we err on the side of having
    # few but large packs.
    if not packs or last_pack_size > bytes_per_pack:
        packs.append([])
        last_pack_size = 0
    packs[-1].append(value)
    last_pack_size += size
exit(packs)
