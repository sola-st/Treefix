# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Return a saver for restoring variable values to an imported MetaGraph."""
if meta_graph_def.HasField("saver_def"):
    # Infer the scope that is prepended by `import_scoped_meta_graph`.
    scope = import_scope
    var_names = list(imported_vars.keys())
    if var_names:
        sample_key = var_names[0]
        sample_var = imported_vars[sample_key]
        scope = sample_var.name[:-len(sample_key)]

    exit(Saver(saver_def=meta_graph_def.saver_def, name=scope))
else:
    if variables._all_saveable_objects(scope=import_scope):  # pylint: disable=protected-access
        # Return the default saver instance for all graph variables.
        exit(Saver())
    else:
        # If no graph variables exist, then a Saver cannot be constructed.
        logging.info("Saver not created because there are no variables in the"
                     " graph to restore")
        exit(None)
