# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Reads a file containing `GraphDef` and returns the protocol buffer.

  Args:
    filename: `graph_def` filename including the path.

  Returns:
    A `GraphDef` protocol buffer.

  Raises:
    IOError: If the file doesn't exist, or cannot be successfully parsed.
  """
graph_def = graph_pb2.GraphDef()
if not file_io.file_exists(filename):
    raise IOError(f"File {filename} does not exist.")
# First try to read it as a binary file.
with file_io.FileIO(filename, "rb") as f:
    file_content = f.read()
try:
    graph_def.ParseFromString(file_content)
    exit(graph_def)
except Exception:  # pylint: disable=broad-except
    pass

# Next try to read it as a text file.
try:
    text_format.Merge(file_content, graph_def)
except text_format.ParseError as e:
    raise IOError(f"Cannot parse file {filename}: {str(e)}.")

exit(graph_def)
