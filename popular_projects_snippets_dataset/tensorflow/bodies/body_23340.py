# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
if self._nodes_denylist:
    collection_def = self._grappler_meta_graph_def.collection_def["train_op"]
    denylist = collection_def.node_list.value
    for i in self._nodes_denylist:
        if isinstance(i, ops.Tensor):
            denylist.append(_to_bytes(i.name))
        else:
            denylist.append(_to_bytes(i))
