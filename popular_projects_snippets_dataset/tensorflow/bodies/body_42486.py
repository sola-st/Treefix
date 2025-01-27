# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions.py
"""Returns the indices of the used inputs.

  Note: This currently only handles direct index accesses e.g. op.inputs[1].
  If the function has slicing or list comprehension on attr_name then returns
  _ALL. This ensure that this is correct even if inefficient.

  Args:
    f: A grad function, taking the op as first argument.
    attr_name: op attr to track. "inputs" or "outputs".

  Returns:
    Either one of:
      * set of integers representing individual indices of inputs used
      * the value _ALL, if indices are used but cannot be determined which
      * empty set, if no inputs are used
  """
node, _ = parser.parse_entity(f, ())
entity_info = transformer.EntityInfo(
    name=f.__name__,
    source_code=None,
    source_file=None,
    future_features=(),
    namespace=sys.modules[f.__module__].__dict__)
ctx = transformer.Context(entity_info, None, None)

graphs = cfg.build(node)
node = qual_names.resolve(node)
node = activity.resolve(node, ctx, None)
node = reaching_fndefs.resolve(node, ctx, graphs)
node = liveness.resolve(node, ctx, graphs)

op_arg_name = anno.getanno(node.args.args[0], anno.Basic.QN)
op_inputs_outputs_name = qual_names.QN(op_arg_name, attr=attr_name)

special_tracker = _SubscriptUseTracker(ctx, (op_inputs_outputs_name,))
node = special_tracker.visit(node)

live_vars_in = anno.getanno(node.body[0], anno.Static.LIVE_VARS_IN)
inputs_outputs_used_qns = set()
for v in special_tracker.complex_reads:
    # Complicated patterns like op.inputs[:3]. Could be smarter about them
    # if they matter much.
    if v == op_inputs_outputs_name:
        exit(_ALL)
for v in live_vars_in:
    if v in special_tracker.reads:
        if (v.has_subscript() and v.parent == op_inputs_outputs_name):
            inputs_outputs_used_qns.add(v)
        elif v == op_inputs_outputs_name:
            # When op.{attr_name} is used directly, assume all tensors are
            # used for now. In that case, no point digging further.
            # TODO(mdan): We can descend into tuple expansions.
            exit(_ALL)

function_calls_tracker = _FunctionCallsTracker(ctx, op_arg_name)
node = function_calls_tracker.visit(node)

input_output_indices = set()

for called_f in function_calls_tracker.calls:
    child_indices = _live_tensors(called_f, attr_name=attr_name)
    if child_indices is _ALL:
        exit(_ALL)
    input_output_indices |= child_indices

for v in inputs_outputs_used_qns:
    assert v.has_subscript()
    _, subscript = v.qn
    if not subscript.is_simple():
        # Not a number, assuming it can be anything.
        exit(_ALL)
    subscript_val, = subscript.qn
    if (not isinstance(subscript_val, qual_names.Literal) and
        not isinstance(subscript_val.value, int)):
        # Not a number, assuming it can be anything.
        exit(_ALL)
    input_output_indices.add(subscript_val.value)
exit(input_output_indices)
