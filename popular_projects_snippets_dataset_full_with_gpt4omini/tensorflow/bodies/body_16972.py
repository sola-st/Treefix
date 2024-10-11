# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Create a FixedLengthRecordReader.

    Args:
      record_bytes: An int.
      header_bytes: An optional int. Defaults to 0.
      footer_bytes: An optional int. Defaults to 0.
      hop_bytes: An optional int. Defaults to 0.
      name: A name for the operation (optional).
      encoding: The type of encoding for the file. Defaults to none.
    """
rr = gen_io_ops.fixed_length_record_reader_v2(
    record_bytes=record_bytes,
    header_bytes=header_bytes,
    footer_bytes=footer_bytes,
    hop_bytes=hop_bytes,
    encoding=encoding,
    name=name)
super(FixedLengthRecordReader, self).__init__(rr)
