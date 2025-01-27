# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/freeze.py
"""Writes a graph def file out to disk.

  Args:
    file_name: Where to save the file.
    frozen_graph_def: GraphDef proto object to save.
  """
tf.io.write_graph(
    frozen_graph_def,
    os.path.dirname(file_name),
    os.path.basename(file_name),
    as_text=False)
tf.compat.v1.logging.info('Saved frozen graph to %s', file_name)
