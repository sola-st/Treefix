# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager.py
"""Restores checkpoint values and SavedModel initializers if found."""
# NOTE: All references to SavedModel refer to SavedModels loaded from the
# load_v2 API (which does not require the `sess` argument).

# If the graph contains resources loaded from a SavedModel, they are not
# restored when calling `saver.restore`. Thus, the SavedModel initializer must
# be called with `saver.restore` to properly initialize the model.

# The SavedModel init is stored in the "saved_model_initializers" collection.
# This collection is part of the MetaGraph's default_init_op, so it is already
# called by MonitoredSession as long as the saver doesn't restore any
# checkpoints from the working dir.
saved_model_init_ops = ops.get_collection("saved_model_initializers")
if saved_model_init_ops:
    sess.run(saved_model_init_ops)

# The saver must be called *after* the SavedModel init, because the SavedModel
# init will restore the variables from the SavedModel variables directory.
# Initializing/restoring twice is not ideal but there's no other way to do it.
saver.restore(sess, path)
