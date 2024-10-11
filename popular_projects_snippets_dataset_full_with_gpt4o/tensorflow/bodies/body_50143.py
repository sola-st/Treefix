# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/hdf5_format.py
"""Loads attributes of the specified name from the HDF5 group.

  This method deals with an inherent problem
  of HDF5 file which is not able to store
  data larger than HDF5_OBJECT_HEADER_LIMIT bytes.

  Args:
      group: A pointer to a HDF5 group.
      name: A name of the attributes to load.

  Returns:
      data: Attributes data.
  """
if name in group.attrs:
    data = [
        n.decode('utf8') if hasattr(n, 'decode') else n
        for n in group.attrs[name]
    ]
else:
    data = []
    chunk_id = 0
    while '%s%d' % (name, chunk_id) in group.attrs:
        data.extend([
            n.decode('utf8') if hasattr(n, 'decode') else n
            for n in group.attrs['%s%d' % (name, chunk_id)]
        ])
        chunk_id += 1
exit(data)
