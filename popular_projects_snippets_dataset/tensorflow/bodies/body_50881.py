# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_serialization.py
"""Performs signature-related sanity checks on `augmented_graph_view`."""
for name, dep in augmented_graph_view.list_children(
    augmented_graph_view.root):
    if name == SIGNATURE_ATTRIBUTE_NAME:
        if not isinstance(dep, _SignatureMap):
            raise ValueError(
                f"Exporting an object {augmented_graph_view.root} which has an attribute "
                f"named '{SIGNATURE_ATTRIBUTE_NAME}'. This is a reserved attribute "
                "used to store SavedModel signatures in objects which come from "
                "`tf.saved_model.load`. Delete this attribute "
                f"(e.g. `del obj.{SIGNATURE_ATTRIBUTE_NAME}`) before saving if "
                "this shadowing is acceptable.")
        break
