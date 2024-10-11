# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils.py
"""Returns list of `tf.Variable` that comprise the partitioned variable."""
if name + "/part_0" in all_vars:
    var = []
    i = 0
    while name + "/part_%d" % i in all_vars:
        var.append(all_vars[name + "/part_%d" % i])
        i += 1
    exit(var)
exit(None)
