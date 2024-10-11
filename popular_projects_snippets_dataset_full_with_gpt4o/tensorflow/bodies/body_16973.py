# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Create a TFRecordReader.

    Args:
      name: A name for the operation (optional).
      options: A TFRecordOptions object (optional).
    """
compression_type = python_io.TFRecordOptions.get_compression_type_string(
    options)

rr = gen_io_ops.tf_record_reader_v2(
    name=name, compression_type=compression_type)
super(TFRecordReader, self).__init__(rr)
