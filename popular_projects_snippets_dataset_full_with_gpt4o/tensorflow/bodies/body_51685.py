# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
# pylint: disable=line-too-long
"""Adds the current meta graph to the SavedModel and saves variables.

    Creates a Saver to save the variables from the provided session. Exports the
    corresponding meta graph def. This function assumes that the variables to be
    saved have been initialized. For a given `SavedModelBuilder`, this API must
    be called exactly once and for the first meta graph to save. For subsequent
    meta graph defs to be added, the `add_meta_graph()` API must be used.

    Args:
      sess: The TensorFlow session from which to save the meta graph and
        variables.
      tags: The set of tags with which to save the meta graph.
      signature_def_map: The map of signature def map to add to the meta graph
        def.
      assets_list: Assets to be saved with SavedModel.
      clear_devices: Set to true if the device info on the default graph should
        be cleared.
      init_op: Op or group of ops to execute when the graph is loaded. Note
          that when the init_op is specified it is run after the restore op at
        load-time.
      train_op: Op or group of ops that trains the model when run. This will
        not be run automatically when the graph is loaded, instead saved in
        a SignatureDef accessible through the exported MetaGraph.
      strip_default_attrs: Boolean. If `True`, default-valued attributes will be
        removed from the NodeDefs. For a detailed guide, see
        [Stripping Default-Valued Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).
      saver: An instance of tf.compat.v1.train.Saver that will be used to export the
        metagraph and save variables. If None, a sharded Saver that restores
        all variables will be used.

    """
# pylint: enable=line-too-long
if self._has_saved_variables:
    raise AssertionError("Graph state including variables and assets has "
                         "already been saved. Please invoke "
                         "`add_meta_graph()` instead.")

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

path_helpers.get_or_create_variables_dir(self._export_dir)
variables_path = path_helpers.get_variables_path(self._export_dir)

saver = self._maybe_create_saver(saver)

# Save the variables. Also, disable writing the checkpoint state proto. The
# file is not used during SavedModel loading. In addition, since a
# SavedModel can be copied or moved, this avoids the checkpoint state to
# become outdated.
saver.save(sess, variables_path, write_meta_graph=False, write_state=False)

# Export the meta graph def.

# The graph almost certainly previously contained at least one Saver, and
# possibly several (e.g. one for loading a pretrained embedding, and another
# for the model weights).  Removing the preexisting ones was the
# motivation for the clear_extraneous_savers option, but it turns out that
# there are edge cases where that option breaks the graph.  Until that is
# resolved, we just leave the option set to False for now.
# TODO(soergel): Reinstate clear_extraneous_savers=True when possible.
meta_graph_def = saver.export_meta_graph(
    clear_devices=clear_devices, strip_default_attrs=strip_default_attrs)

# Save asset files and write them to disk, if any.
self._save_and_write_assets(meta_graph_def, assets_list)

# Tag the meta graph def and add it to the SavedModel.
self._tag_and_add_meta_graph(meta_graph_def, tags, signature_def_map)

# Mark this instance of SavedModel as having saved variables, such that
# subsequent attempts to save variables will fail.
self._has_saved_variables = True
