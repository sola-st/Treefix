# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2.py
"""Restores variables from the checkpoint."""
if restore_from_saver is not None:
    initializer, _ = restore_from_saver(
        constant_op.constant(self._variables_path))
    if not ops.executing_eagerly_outside_functions():
        # Add the initialization operation to the "saved_model_initializers"
        # collection in case we don't have any lifted variables to attach it to.
        ops.add_to_collection("saved_model_initializers", initializer)
        one_unlifted = False

        for variable in wrapped.graph.get_collection_ref(
            ops.GraphKeys.GLOBAL_VARIABLES):
            if variable.graph is wrapped.graph:
                one_unlifted = True
            # pylint: disable=protected-access
            variable._initializer_op = initializer
            # pylint: enable=protected-access
        if one_unlifted:
            logging.warning(
                "Some variables could not be lifted out of a loaded function. "
                "Please run "
                "`sess.run(tf.get_collection(\"saved_model_initializers\"))`to "
                "restore these variables.")
