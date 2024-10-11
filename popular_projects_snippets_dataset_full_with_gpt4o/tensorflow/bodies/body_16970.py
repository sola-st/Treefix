# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Create a WholeFileReader.

    Args:
      name: A name for the operation (optional).
    """
rr = gen_io_ops.whole_file_reader_v2(name=name)
super(WholeFileReader, self).__init__(rr, supports_serialize=True)
