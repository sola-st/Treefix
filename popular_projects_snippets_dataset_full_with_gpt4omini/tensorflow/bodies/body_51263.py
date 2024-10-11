# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Saves a SavedModel while returning all saved nodes and their paths.

  Please see `tf.saved_model.save` for details.

  Args:
    obj: A trackable object to export.
    export_dir: A directory in which to write the SavedModel.
    signatures: A function or dictionary of functions to save in the SavedModel
      as signatures.
    options: `tf.saved_model.SaveOptions` object for configuring save options.
    experimental_skip_checkpoint: If set to `True`, the checkpoint will not be
      written.

  Returns:
    A tuple of (a list of saved nodes in the order they are serialized to the
      `SavedObjectGraph`, dictionary mapping nodes to one possible path from
      the root node to the key node)
  """
options = options or save_options.SaveOptions()
# TODO(b/205008509): Factor out some subset of SavedModelBuilder which is 2.x
# compatible (no sessions) and share it with this export API rather than
# making a SavedModel proto and writing it directly.
saved_model = saved_model_pb2.SavedModel()
meta_graph_def = saved_model.meta_graphs.add()

_, exported_graph, object_saver, asset_info, saved_nodes, node_paths = (
    _build_meta_graph(obj, signatures, options, meta_graph_def))
saved_model.saved_model_schema_version = (
    constants.SAVED_MODEL_SCHEMA_VERSION)

# Write the checkpoint, copy assets into the assets directory, and write out
# the SavedModel proto itself.
if not experimental_skip_checkpoint:
    path_helpers.get_or_create_variables_dir(export_dir)
    ckpt_options = checkpoint_options.CheckpointOptions(
        experimental_io_device=options.experimental_io_device)
    object_saver.save(
        path_helpers.get_variables_path(export_dir), options=ckpt_options)
builder_impl.copy_assets_to_destination_dir(asset_info.asset_filename_map,
                                            export_dir)
# Note that this needs to be the last file operation when saving the
# SavedModel. Users rely on checking saved_model_dir/saved_model.pb as an
# indication that the SavedModel is completely written.
if context.executing_eagerly():
    try:
        context.async_wait()  # Ensure save operations have completed.
    except errors.NotFoundError as err:
        raise FileNotFoundError(
            f"{err}\n You may be trying to save on a different device from the "
            "computational device. Consider setting the "
            "`experimental_io_device` option in `tf.saved_model.SaveOptions` "
            "to the io_device such as '/job:localhost'.")

  # We will slowly migrate code in this function to pywrap_saved_model.Save
  # as we build up the C++ API.
pywrap_saved_model.Save(export_dir)

saved_model_serialized = saved_model.SerializeToString(deterministic=True)

# Write fingerprint protobuf, if requested.
if flags.config().saved_model_fingerprinting.value():
    fingerprint_path = file_io.join(
        compat.as_str(export_dir),
        compat.as_str(constants.FINGERPRINT_FILENAME))
    fingerprint_serialized = fingerprinting.CreateFingerprintDef(
        saved_model_serialized, export_dir)
    file_io.atomic_write_string_to_file(fingerprint_path,
                                        fingerprint_serialized)
    # We need to deserialize the fingerprint in order to send its values.
    fingerprint_proto = fingerprint_pb2.FingerprintDef()
    fingerprint_proto.ParseFromString(fingerprint_serialized)
    metrics.SetWriteFingerprint(
        saved_model_checksum=str(fingerprint_proto.saved_model_checksum))

path = file_io.join(
    compat.as_str(export_dir),
    compat.as_str(constants.SAVED_MODEL_FILENAME_PB))
file_io.atomic_write_string_to_file(
    path, saved_model.SerializeToString(deterministic=True))

# Save debug info, if requested.
if options.save_debug_info:
    _export_debug_info(exported_graph, export_dir)
# Clean reference cycles so repeated export()s don't make work for the garbage
# collector. Before this point, we need to keep references to captured
# constants in the saved graph.
ops.dismantle_graph(exported_graph)

exit((saved_nodes, node_paths))
