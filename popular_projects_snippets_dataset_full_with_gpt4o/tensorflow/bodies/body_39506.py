# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Asserts that all objects in the checkpoint have been created/matched.

    Returns:
      `self` for chaining.
    Raises:
      AssertionError: If there are any Python objects in the dependency graph
        which have not been restored from this checkpoint or a later `restore`,
        or if there are any checkpointed values which have not been matched to
        Python objects.
    """
pretty_printer = ObjectGraphProtoPrettyPrinter(
    self._checkpoint.object_graph_proto)
self.assert_existing_objects_matched()
for node_id, node in enumerate(self._checkpoint.object_graph_proto.nodes):
    if not node.attributes:
        # Only raise exceptions for the nodes with attributes themselves. Either
        # they're ultimately not important, or they have a child with an
        # attribute.
        continue
    trackable = self._checkpoint.object_by_proto_id.get(node_id, None)
    if trackable is None:
        raise AssertionError(
            "Unresolved object in checkpoint "
            f"{pretty_printer.node_names[node_id]}: {node}")
if self._checkpoint.slot_restorations:
    # Sanity check; this collection should be clear if everything has been
    # restored.
    raise AssertionError(
        f"Unresolved slot restorations: {self._checkpoint.slot_restorations}")
if self._checkpoint.unused_attributes:
    unused_attribute_messages = []
    for node_id, attribute in self._checkpoint.unused_attributes.items():
        obj = self._checkpoint.object_by_proto_id[node_id]
        unused_attribute_messages.append(
            f"{pretty_printer.node_names[node_id]} ({obj}): {attribute}")
    joined_attribute_messages = "\n".join(unused_attribute_messages)
    raise AssertionError(
        "Unused attributes in these objects (the attributes exist in the "
        f"checkpoint but were not restored):\n{joined_attribute_messages}")
exit(self)
