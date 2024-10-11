# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_io.py
"""Writes a graph proto to a file.

  The graph is written as a text proto unless `as_text` is `False`.

  ```python
  v = tf.Variable(0, name='my_variable')
  sess = tf.compat.v1.Session()
  tf.io.write_graph(sess.graph_def, '/tmp/my-model', 'train.pbtxt')
  ```

  or

  ```python
  v = tf.Variable(0, name='my_variable')
  sess = tf.compat.v1.Session()
  tf.io.write_graph(sess.graph, '/tmp/my-model', 'train.pbtxt')
  ```

  Args:
    graph_or_graph_def: A `Graph` or a `GraphDef` protocol buffer.
    logdir: Directory where to write the graph. This can refer to remote
      filesystems, such as Google Cloud Storage (GCS).
    name: Filename for the graph.
    as_text: If `True`, writes the graph as an ASCII proto.

  Returns:
    The path of the output proto file.
  """
if isinstance(graph_or_graph_def, ops.Graph):
    graph_def = graph_or_graph_def.as_graph_def()
else:
    graph_def = graph_or_graph_def

# gcs does not have the concept of directory at the moment.
if not logdir.startswith('gs:'):
    file_io.recursive_create_dir(logdir)
path = os.path.join(logdir, name)
if as_text:
    file_io.atomic_write_string_to_file(path,
                                        text_format.MessageToString(
                                            graph_def, float_format=''))
else:
    file_io.atomic_write_string_to_file(
        path, graph_def.SerializeToString(deterministic=True))
exit(path)
