# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
"""Adds the current meta graph to the SavedModel.

    Creates a Saver in the current scope and uses the Saver to export the meta
    graph def. Invoking this API requires the `add_meta_graph_and_variables()`
    API to have been invoked before.

    Args:
      tags: The set of tags to annotate the meta graph def with.
      signature_def_map: The map of signature defs to be added to the meta graph
        def.
      assets_list: Assets to be saved with SavedModel. Note
          that this list should be a subset of the assets saved as part of
          the first meta graph in the SavedModel.
      clear_devices: Set to true if the device info on the default graph should
        be cleared.
      init_op: Op or group of ops to execute when the graph is loaded. Note
          that when the init_op is specified it is run after the restore op at
        load-time.
      train_op: Op or group of opts that trains the model when run. This will
        not be run automatically when the graph is loaded, instead saved in
        a SignatureDef accessible through the exported MetaGraph.
      saver: An instance of tf.compat.v1.train.Saver that will be used to export
        the metagraph. If None, a sharded Saver that restores all variables will
        be used.

    Raises:
      AssertionError: If the variables for the SavedModel have not been saved
          yet, or if the graph already contains one or more legacy init ops.
    """
if not self._has_saved_variables:
    raise AssertionError(
        "Graph state including variables and assets has not been saved yet. "
        "Please invoke `add_meta_graph_and_variables()` first.")

# Validate the signature def map to ensure all included TensorInfos are
# properly populated.
signature_def_map = signature_def_map or {}
self._validate_signature_def_map(signature_def_map)

# Create a SignatureDef pointing to the graph initialization op, which will
# be added to the MetaGraphDef.
_add_op_to_signature_def_map(signature_def_map, init_op,
                             constants.INIT_OP_SIGNATURE_KEY)
_add_op_to_signature_def_map(signature_def_map, train_op,
                             constants.TRAIN_OP_SIGNATURE_KEY)

saver = self._maybe_create_saver(saver)

# The graph almost certainly previously contained at least one Saver, and
# possibly several (e.g. one for loading a pretrained embedding, and another
# for the model weights).  Removing the preexisting ones was the
# motivation for the clear_extraneous_savers option, but it turns out that
# there are edge cases where that option breaks the graph.  Until that is
# resolved, we just leave the option set to False for now.
# TODO(soergel): Reinstate clear_extraneous_savers=True when possible.
meta_graph_def = saver.export_meta_graph(
    clear_devices=clear_devices, strip_default_attrs=True)

# Save asset files and write them to disk, if any.
self._save_and_write_assets(meta_graph_def, assets_list)

# Tag the meta graph def and add it to the SavedModel.
self._tag_and_add_meta_graph(meta_graph_def, tags, signature_def_map)
