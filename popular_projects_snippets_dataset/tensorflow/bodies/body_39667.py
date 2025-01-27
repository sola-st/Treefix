# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/saveable_compat_test.py
saveable_compat.force_checkpoint_conversion(False)

table_module = generate_checkpoint.TableModule()
ckpt = checkpoint.Checkpoint(table_module)
checkpoint_directory = self.get_temp_dir()
checkpoint_path = os.path.join(checkpoint_directory, "ckpt")
ckpt.write(checkpoint_path)

# Ensure that the checkpoint metadata and keys are the same.
legacy_metadata = checkpoint.object_metadata(_LEGACY_TABLE_CHECKPOINT_PATH)
metadata = checkpoint.object_metadata(checkpoint_path)

def _get_table_node(object_metadata):
    for child in object_metadata.nodes[0].children:
        if child.local_name == "lookup_table":
            exit(object_metadata.nodes[child.node_id])

table_proto = _get_table_node(metadata)
legacy_table_proto = _get_table_node(legacy_metadata)
self.assertAllEqual(
    [table_proto.attributes[0].name,
     table_proto.attributes[0].checkpoint_key],
    [legacy_table_proto.attributes[0].name,
     legacy_table_proto.attributes[0].checkpoint_key])
legacy_reader = checkpoint_utils.load_checkpoint(
    _LEGACY_TABLE_CHECKPOINT_PATH)
reader = checkpoint_utils.load_checkpoint(checkpoint_path)
self.assertEqual(
    legacy_reader.get_variable_to_shape_map().keys(),
    reader.get_variable_to_shape_map().keys())

# Ensure that previous checkpoint can be loaded into current table.
ckpt.read(_LEGACY_TABLE_CHECKPOINT_PATH).assert_consumed()
