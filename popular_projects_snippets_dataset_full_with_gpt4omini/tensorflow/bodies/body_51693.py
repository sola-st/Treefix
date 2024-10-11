# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
if self._has_saved_variables:
    raise AssertionError("Graph state including variables and assets has "
                         "already been saved. Please invoke "
                         "`add_meta_graph()` instead.")

# Validate the signature def map to ensure all included TensorInfos are
# properly populated.
signature_def_map = signature_def_map or {}
self._validate_signature_def_map(signature_def_map)

# legacy_init_op is deprecated, and going away in TF 2.0.
# Re-mapping to main_op, as treatment is identical regardless.
main_op = main_op or legacy_init_op

# Add assets and ops
self._add_collections(assets_collection, main_op, None)

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

# Tag the meta graph def and add it to the SavedModel.
self._tag_and_add_meta_graph(meta_graph_def, tags, signature_def_map)

# Mark this instance of SavedModel as having saved variables, such that
# subsequent attempts to save variables will fail.
self._has_saved_variables = True
