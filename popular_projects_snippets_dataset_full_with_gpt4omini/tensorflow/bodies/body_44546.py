# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Verifies loop variables for consistency."""
if check_shapes and 'shape_invariants' in opts:
    shape_invariants = opts['shape_invariants']
else:
    shape_invariants = nest.map_structure(lambda _: None, iter_entry_vars)

assert len(symbol_names) == len(shape_invariants)
assert len(symbol_names) == len(init_vars)
assert len(symbol_names) == len(iter_entry_vars)
assert len(symbol_names) == len(iter_exit_vars)

for i in range(len(symbol_names)):
    name = symbol_names[i]
    init = init_vars[i]
    entry = iter_entry_vars[i]
    exit_ = iter_exit_vars[i]
    invariant = shape_invariants[i]

    try:
        nest.assert_same_structure(init, entry, expand_composites=True)
    except (ValueError, TypeError):
        # `Variable`s in `init` may be implicitly converted to `Tensor`s. Convert
        # `ResourceVariable`s to Tensors so tf.nest.assert_same_structure
        # won't break due to type spec mismatches between `ResourceVariable`s and
        # `Tensor`s.
        try:
            init_tensors = variable_utils.convert_variables_to_tensors(init)
            nest.assert_same_structure(init_tensors, entry, expand_composites=True)
        except (ValueError, TypeError) as e:
            raise TypeError("'{}' does not have the same nested structure after one"
                            ' iteration.\n\n{}'.format(name, e)) from e

    try:
        nest.assert_same_structure(entry, exit_, expand_composites=True)
    except (ValueError, TypeError) as e:
        raise TypeError("'{}' does not have the same nested structure after one"
                        ' iteration.\n\n{}'.format(name, e)) from e
    if invariant is not None:
        try:
            nest.assert_same_structure(init, invariant, expand_composites=False)
        except (ValueError, TypeError) as e:
            raise TypeError("'{}' does not have the same nested structure as its"
                            ' corresponding shape invariant.\n\n{}'.format(
                                name, e)) from e

    nest.map_structure(
        functools.partial(_verify_single_loop_var, name, check_shapes), init,
        entry, exit_, invariant)
