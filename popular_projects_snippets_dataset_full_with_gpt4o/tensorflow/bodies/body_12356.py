# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/custom_gradient.py
"""Inner function closure for calculating gradients."""
current_var_scope = variable_scope.get_variable_scope()
with tape_lib.stop_recording():
    result = f(*args, **kwargs)

def grad_wrapper(*wrapper_args, variables=None):
    """Wrapper function to accomodate lack of kwargs in graph mode custom_gradient."""

    @custom_gradient
    def inner_recompute_grad(*dresult):
        """Nested custom gradient function for computing grads in reverse and forward mode autodiff."""
        # Gradient calculation for reverse mode autodiff.
        with backprop.GradientTape() as t:
            id_args = nest.map_structure(gen_array_ops.identity, args)
            # Tuple `dresult` should contain at least one tensor.
            assert len(dresult) >= 1

            if not context.executing_eagerly():
                # XLA doesn't respect `tf.control_dependencies`. The code block
                # below manually adds a data dependency to `dresult` to ensure
                # recomputation of `f(*args, **kwargs)` happens after `dresult`.

                # This works even if `dresult[0]` is a size 0 tensor as reduce_max
                # of a size 0 tensor returns -inf. Use reshape here to avoid reading
                # the entire `dresult[0]`.
                elem = math_ops.reduce_max(array_ops.reshape(dresult[0], [-1])[:1])
                # Cast elem to bool in case elem is NaN.
                elem_bool = math_ops.cast(elem, dtypes.bool)
                dresult_dep = array_ops.where_v2(
                    elem_bool == elem_bool, 0., float("nan"))  # pylint: disable=comparison-with-itself
                id_args = nest.map_structure(
                    lambda x: x + math_ops.cast(dresult_dep, x.dtype), id_args)

            t.watch(id_args)
            if variables is not None:
                t.watch(variables)
            with variable_scope.variable_scope(current_var_scope):
                recomputed_result = f(*id_args, **kwargs)
        kw_vars = []
        if variables is not None:
            kw_vars = list(variables)
        grads = t.gradient(
            recomputed_result,
            list(id_args) + kw_vars,
            output_gradients=dresult,
            unconnected_gradients=UnconnectedGradients.ZERO)

        def transpose(*t_args, **t_kwargs):
            """Gradient function calculation for forward mode autodiff."""
            # Just throw an error since gradients / activations are not stored on
            # tape for recompute.
            raise NotImplementedError(
                "recompute_grad tried to transpose grad of {}. "
                "Consider not using recompute_grad in forward mode"
                "autodiff".format(f.__name__))

        exit(((grads[:len(id_args)], grads[len(id_args):]), transpose))

    exit(inner_recompute_grad(*wrapper_args))

exit((result, grad_wrapper))
