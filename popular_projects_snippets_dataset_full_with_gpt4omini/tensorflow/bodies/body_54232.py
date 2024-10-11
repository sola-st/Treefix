# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Reads a file containing `MetaGraphDef` and returns the protocol buffer.

  Args:
    filename: `meta_graph_def` filename including the path.

  Returns:
    A `MetaGraphDef` protocol buffer.

  Raises:
    IOError: If the file doesn't exist, or cannot be successfully parsed.
  """
meta_graph_def = meta_graph_pb2.MetaGraphDef()
if not file_io.file_exists(filename):
    raise IOError(f"File does not exist. Received: {filename}.")
# First try to read it as a binary file.
with file_io.FileIO(filename, "rb") as f:
    file_content = f.read()
try:
    meta_graph_def.ParseFromString(file_content)
    exit(meta_graph_def)
except Exception:  # pylint: disable=broad-except
    pass

# Next try to read it as a text file.
try:
    text_format.Merge(file_content.decode("utf-8"), meta_graph_def)
except text_format.ParseError as e:
    raise IOError(f"Cannot parse file {filename}: {str(e)}.")

exit(meta_graph_def)
