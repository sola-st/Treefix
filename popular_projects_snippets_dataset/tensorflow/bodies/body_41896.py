# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Initialize a `ConcreteFunction`.

    Args:
      func_graph: An instance of FuncGraph: the function body to wrap.
      attrs: (optional) dict mapping names of attributes to their AttrValue
        values. Attributes in `attrs` will be included in this function's
        definition.
     shared_func_graph: If False, the ConcreteFunction takes ownership of
       `func_graph` and will break reference cycles when it is deleted. This
       makes the FuncGraph inoperable.
     spec: FunctionSpec for the original function.  If not specified, then this
       ConcreteFunction may only be called using the flat signature.

    Raises:
      ValueError: If number of input_placeholders is not equal to the number
        of function inputs.
    """
# _arg_keywords and _num_positional_args define the flat signature.  They
# are assigned after construction.
self._arg_keywords = None
self._num_positional_args = None

self._func_graph = func_graph
self._captured_inputs = self._func_graph.external_captures + self._func_graph.deferred_external_captures

# spec defines the structured signature.
self._set_function_spec(spec)

if attrs and attributes_lib.IMPLEMENTS in attrs:
    # The alternative is to silently drop "implements" tag
    # but it seems likely it would lead to hard to catch bugs.
    # Another alternative is to make func_body to preserve the order
    # of arguments if variables are present. Yet another option
    # is to automatically replace variables as arguments to functions
    # to v.read_value() whenever "implements" tag is present
    # Anytime we annotate existing function we probably want to wrap
    # it with safe read_value for backward compatibility.
    has_resource_vars = any(
        inp.dtype == dtypes.resource for inp in self.inputs)

    assert not any((has_resource_vars, self._captured_inputs)), (
        'Function {name} has "{attr}={value}" attribute and thus can not '
        "depend on any tensors outside of its signature or modify variables. "
        "\n\nNote: variables are always captured and cause function "
        "re-tracing for every variable called.\n"
        "  inputs: {inputs}\n  captures: {captured}\n\n"
        "To pass a variable to such function use  "
        "use variable.read_value().".format(
            name=func_graph.name,
            attr=attributes_lib.IMPLEMENTS,
            value=attrs[attributes_lib.IMPLEMENTS],
            inputs=self.inputs,
            captured=self._captured_inputs))
self._output_shapes = tuple(
    output.shape for output in self._func_graph.outputs)
self._attrs = _parse_func_attrs(attrs or {})

if shared_func_graph:
    self._garbage_collector = None
else:
    self._garbage_collector = ConcreteFunctionGarbageCollector(func_graph)

# Pairs of forward and backward functions used for computing gradients.
#
# These each get a reference to the FuncGraph deleter since they use the
# FuncGraph directly.
self._delayed_rewrite_functions = _DelayedRewriteGradientFunctions(
    func_graph, self._attrs, self._garbage_collector)
self._first_order_tape_functions = {}
self._higher_order_tape_functions = {}
# Cache the inference function to avoid a (Python) function call when not
# building gradients.
self._inference_function = self._delayed_rewrite_functions.forward()
