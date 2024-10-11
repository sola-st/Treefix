# Extracted from ./data/repos/tensorflow/tensorflow/examples/label_image/label_image.py
graph = tf.Graph()
graph_def = tf.GraphDef()

with open(model_file, "rb") as f:
    graph_def.ParseFromString(f.read())
with graph.as_default():
    tf.import_graph_def(graph_def)

exit(graph)
