# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/item.py
if self._item_graph != self._metagraph:
    self._BuildTFItem()
    self._item_graph.CopyFrom(self._metagraph)
exit(self._tf_item)
