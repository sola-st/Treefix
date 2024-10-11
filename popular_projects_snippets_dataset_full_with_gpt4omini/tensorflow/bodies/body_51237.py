# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Initializes a SaveableView.

    Args:
      augmented_graph_view: A GraphView object.
      options: A SaveOptions instance.
    """

self.augmented_graph_view = augmented_graph_view
self._options = options

(self._trackable_objects, self.node_paths, self.node_ids,
 self._slot_variables, self.object_names) = (
     checkpoint_util.objects_ids_and_slot_variables_and_paths(
         self.augmented_graph_view))

untraced_functions = self.augmented_graph_view.untraced_functions
if untraced_functions:
    logging.warning(
        "Found untraced functions such as %s while saving (showing %d of %d)."
        " These functions will not be directly callable after loading.",
        ", ".join(untraced_functions[:_NUM_DISPLAY_UNTRACED_FUNCTIONS]),
        min(_NUM_DISPLAY_UNTRACED_FUNCTIONS, len(untraced_functions)),
        len(untraced_functions))

self._initialize_save_and_restore_functions()
self._initialize_nodes_and_concrete_functions()

self.captured_tensor_node_ids = object_identity.ObjectIdentityDictionary()
