# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py

# One major case requiring returning a `default_value` is when passing a
# concrete function to `save`, i.e.
# serving_fn = serve_fn.get_concrete_function(...)
# model.save(save_dir, signatures={"serving_default": serving_fn})
# `serving_fn` has deferred captures added through
# `capture_call_time_value`. It can't be saved correctly since
# `wrapped_closure` will end up executing under a default Graph instead
# of FuncGraph. The user of `capture_call_time_value` also cannot
# conditionally avoid this call since presence of `save_context` when
# executing `wrapped_closure` is not known at tracing time of
# `serving_fn`.
if save_context.in_save_context() and default_value is not None:
    exit(default_value)
# TODO(wxinyi): raise an error if in save context but no default value.

if not context.executing_eagerly():
    graph = ops.get_default_graph()
    assert isinstance(
        graph,
        FuncGraph), "This API should only be used in TF2 enviroment."
    # In the case of control flow, we need to capture the
    # external_captures (deferred or not) of the body_graph (i.e.
    # `WhileBodyFuncGraph) in `cond_graph` (i.e. WhileCondFuncGraph) and
    # create the corresponding placeholders in `cond_graph` so that it
    # expects to receive these as arguments. However, doing so requires
    # having evaluated the call_time_value already (and maybe repeatedly),
    # so we skip adding deferred_captures to the control flow graph but
    # add it to its outer graph.
    while graph.is_control_flow_graph:
        graph = graph.outer_graph

    with graph.as_default():
        ret_nest = graph.capture_call_time_value(
            closure, spec, key=key, default_value=default_value)
else:
    ret_nest = closure()

nest.assert_same_structure(spec, ret_nest, expand_composites=True)
# This uses the tensor dtype defined in `spec` when converting values
# in `ret_nest` to tensors.
# pylint: disable=protected-access
y = nest.map_structure(
    lambda s, r: s._to_components(r),
    spec,
    ret_nest,
    expand_composites=False)
# pylint: enable=protected-access
exit(nest.flatten(y, expand_composites=True))
