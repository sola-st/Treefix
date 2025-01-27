# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/item.py
self._tf_item = tf_item.TF_NewItem(self._metagraph.SerializeToString(),
                                   self._ignore_colocation,
                                   self._ignore_user_placement)
