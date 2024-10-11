# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Verifies variables manipulated by a conditional for consistency."""
named_vars = zip(symbol_names, body_vars, orelse_vars)

for name, body_var, orelse_var in named_vars:
    try:
        nest.assert_same_structure(body_var, orelse_var, expand_composites=True)
    except (ValueError, TypeError):
        # One branch of cond could be a `Tensor`, while the other branch could be
        # a `ResourceVariable`. Convert `ResourceVariable`s to `Tensor`s so
        # assert_same_structure won't fail.
        try:
            body_var_tensors = variable_utils.convert_variables_to_tensors(body_var)
            orelse_var_tensors = variable_utils.convert_variables_to_tensors(
                orelse_var)
            nest.assert_same_structure(body_var_tensors, orelse_var_tensors,
                                       expand_composites=True)
        except (ValueError, TypeError) as e:
            raise TypeError(
                "'{}' must have the same nested structure in the main and else"
                ' branches:\n\n{}'.format(name, str(e))) from e
    nest.map_structure(
        functools.partial(verify_single_cond_var, name), body_var, orelse_var)
