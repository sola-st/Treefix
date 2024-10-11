# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
self.eager_op_types = []
self.eager_op_names = []
self.eager_attrs = []
self.eager_graphs = []
self.eager_inputs = []
self.graph_op_types = []
self.graph_op_names = []
self.graph_attrs = []
self.graph_graphs = []
self.graph_graph_versions = []
self.graph_inputs = []

# A dict mapping tensor name (e.g., "MatMut_10") to a list of ndarrays.
# The list is the history of the tensor's computation result inside
# `tf.Graph`s (`FuncGraph`s).
# For an op with multiple output tensors, the outputs are interleaved in
# the list.
self.graph_internal_ndarrays = {}
