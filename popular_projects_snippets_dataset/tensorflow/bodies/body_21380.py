# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
err_msg = ("Restoring from checkpoint failed. This is most likely "
           "due to {} from the checkpoint. Please ensure that you "
           "have not altered the graph expected based on the checkpoint. "
           "Original error:\n\n{}").format(extra_verbiage, err.message)
exit(err.__class__(err.node_def, err.op, err_msg))
