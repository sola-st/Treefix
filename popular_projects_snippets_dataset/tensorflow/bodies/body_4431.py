# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/test_streaming_accuracy.py
"""Read a tensorflow model, and creates a default graph object."""
graph = tf.Graph()
with graph.as_default():
    od_graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(mode_file, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')
exit(graph)
