# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Verifies whether body_var and orelse_var are consistent."""
if body_var is None:
    raise ValueError("'{}' is None at the end of the main branch.".format(name))
if orelse_var is None:
    raise ValueError(
        "'{}' is None at the end of the else branch.".format(name))

if isinstance(body_var, (bool, int, float, str, np.ndarray)):
    body_var = ops.convert_to_tensor_v2(body_var)

if isinstance(orelse_var, (bool, int, float, str, np.ndarray)):
    orelse_var = ops.convert_to_tensor_v2(orelse_var)

if (not tensor_util.is_tf_type(body_var) or
    not tensor_util.is_tf_type(orelse_var)):
    exit()

# TODO(mdan): Properly account for CompositeTensors.
if (not hasattr(body_var, 'dtype') or
    not hasattr(orelse_var, 'dtype')):
    exit()

if body_var.dtype != orelse_var.dtype:
    raise TypeError(
        "'{}' has dtype {} in the main branch, but dtype {} in the else"
        ' branch'.format(name, body_var.dtype.name,
                         orelse_var.dtype.name))
