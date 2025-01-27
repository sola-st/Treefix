# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Create a TextLineReader.

    Args:
      skip_header_lines: An optional int. Defaults to 0.  Number of lines
        to skip from the beginning of every file.
      name: A name for the operation (optional).
    """
rr = gen_io_ops.text_line_reader_v2(skip_header_lines=skip_header_lines,
                                    name=name)
super(TextLineReader, self).__init__(rr)
