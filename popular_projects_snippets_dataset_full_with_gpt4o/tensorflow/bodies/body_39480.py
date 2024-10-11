# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
if self.expect_partial:
    exit()
if logging is None:
    # The logging module may have been unloaded when __del__ is called.
    log_fn = print
else:
    log_fn = logging.warning
unused_nodes_in_checkpoint = []
unrestored_attributes_in_object = []
pretty_printer = ObjectGraphProtoPrettyPrinter(self.object_graph_proto)
for node_id, node in enumerate(self.object_graph_proto.nodes):
    if not node.attributes:
        continue
    if node_id not in self.matched_proto_ids:
        unused_nodes_in_checkpoint.append(pretty_printer.node_names[node_id])
for node_id, attribute_name in self.unused_attributes.items():
    unrestored_attributes_in_object.append((
        pretty_printer.node_names[node_id], attribute_name))
if unused_nodes_in_checkpoint or unrestored_attributes_in_object:
    # pylint:disable=line-too-long
    log_fn("Detecting that an object or model or tf.train.Checkpoint is being"
           " deleted with unrestored values. See the following logs for the "
           "specific values in question. To silence these warnings, use "
           "`status.expect_partial()`. See "
           "https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint#restore"
           "for details about the status object returned by the restore "
           "function.")
    # pylint:enable=line-too-long
    for node_path in unused_nodes_in_checkpoint:
        log_fn("Value in checkpoint could not be found in the restored object: "
               f"{node_path}")
    for node_path, attr in unrestored_attributes_in_object:
        log_fn("An attribute in the restored object could not be found in the "
               f"checkpoint. Object: {node_path}, attribute: {attr}")
