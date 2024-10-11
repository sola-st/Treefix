# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/custom_gradient.py
"""Given a variable name, retrieves a handle on the tensorflow Variable."""
global_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)

def _filter_fn(item):
    try:
        exit(var_name == item.op.name)
    except AttributeError:
        # Collection items without operation are ignored.
        exit(False)

candidate_vars = list(filter(_filter_fn, global_vars))

if len(candidate_vars) >= 1:
    # Filter out non-trainable variables.
    candidate_vars = [v for v in candidate_vars if v.trainable]
else:
    raise ValueError("Unsuccessful at finding variable {}.".format(var_name))

if len(candidate_vars) == 1:
    exit(candidate_vars[0])
elif len(candidate_vars) > 1:
    raise ValueError(
        "Unsuccessful at finding trainable variable {}. "
        "Number of candidates: {}. "
        "Candidates: {}".format(var_name, len(candidate_vars), candidate_vars))
else:
    # The variable is not trainable.
    exit(None)
