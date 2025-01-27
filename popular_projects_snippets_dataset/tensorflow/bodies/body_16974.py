# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Create a LMDBReader.

    Args:
      name: A name for the operation (optional).
      options: A LMDBRecordOptions object (optional).
    """
del options
rr = gen_io_ops.lmdb_reader(name=name)
super(LMDBReader, self).__init__(rr)
