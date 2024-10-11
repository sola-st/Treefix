# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
node_def = node_def_pb2.NodeDef()
node_def.CopyFrom(self.node_def)
# Used in TPUReplicateContext to indicate whether this node has been cloned
# and to not add TPU attributes.
node_def.attr['_cloned'].b = True
node_def.name = graph.unique_name(node_def.name)
exit(node_def)
