# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/label_wav.py
"""Unpersists graph from file as default graph."""
with tf.io.gfile.GFile(filename, 'rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')
