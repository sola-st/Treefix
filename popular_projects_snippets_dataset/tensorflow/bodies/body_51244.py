# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
node_id = len(self.nodes)
self.nodes.append(node)
self.node_ids[capture] = node_id
self.node_ids[node] = node_id
self.captured_tensor_node_ids[capture] = node_id
exit(node_id)
