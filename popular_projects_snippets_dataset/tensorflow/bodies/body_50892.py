# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2.py
"""Called from wrap_function to import `meta_graph_def`."""
# pylint: disable=protected-access
saver, _ = tf_saver._import_meta_graph_with_return_elements(
    meta_graph_def)
# pylint: enable=protected-access
returns[0] = saver
