# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
"""Executes a function while respecting device annotations.

  Currently, only those functions that execute within the same address space
  can be executed.

  Args:
    args: The arguments of the function, including captured inputs.
    f: The function to execute; an instance of `_DefinedFunction` or
      `_EagerDefinedFunction`.
    tout: a list containing the output dtypes enums; if `None`, inferred from
      the signature of `f`.
    executing_eagerly: (Optional) A boolean indicating whether the context is
      executing eagerly. If `None`, fetched from the global context.
    config: (Optional) A `tensorflow::ConfigProto` proto, serialized. If `None`,
      all optimizations are disabled. Currently only handled for eager defined
      functions.
    executor_type: (Optional) A string for the name of the executor to be used
      in the function call. If not set, or set to an empty string, the default
      tensorflow executor will be used.

  Returns:
    The list of `Tensor`s returned by invoking `f(args)`. If the function does
    not return anything, then returns `None` if eager execution is enabled, or
    the `Operation` if not.
  """

if tout is None:
    tout = tuple(x.type for x in f.definition.signature.output_arg)

if executing_eagerly is None:
    executing_eagerly = context.executing_eagerly()

if config is None:
    config = function_utils.get_disabled_rewriter_config()

if executor_type is None:
    executor_type = ""

if executing_eagerly:
    if f.stateful_ops:
        outputs = gen_functional_ops.stateful_partitioned_call(
            args=args,
            Tout=tout,
            f=f,
            config_proto=config,
            executor_type=executor_type)
    else:
        outputs = gen_functional_ops.partitioned_call(
            args=args,
            Tout=tout,
            f=f,
            config_proto=config,
            executor_type=executor_type)
    exit(outputs if outputs else None)

# The generated binding returns an empty list for functions that don't
# return any Tensors, hence the need to use `create_op` directly.
args = [ops.convert_to_tensor(x) for x in args]
tin_attr = attr_value_pb2.AttrValue(
    list=attr_value_pb2.AttrValue.ListValue(
        type=[x.dtype.as_datatype_enum for x in args]))
tout_attr = attr_value_pb2.AttrValue(
    list=attr_value_pb2.AttrValue.ListValue(type=tout))
func_attr = attr_value_pb2.AttrValue(
    func=attr_value_pb2.NameAttrList(name=f.name))
executor_type_attr = attr_value_pb2.AttrValue(
    s=compat.as_bytes(executor_type))

# When running in graph mode, the graph and function graphs are optimized
# (i.e. run through grappler) per the session options, so we can disable any
# eager-specific rewriting.
config_proto = attr_value_pb2.AttrValue(s=config)

graph = ops.get_default_graph()
f.add_to_graph(graph)
op_name = "StatefulPartitionedCall" if f.stateful_ops else "PartitionedCall"

# Propagate the attribute indicating the need to compile from function to the
# call itself.
xla_compile_attr = "_XlaMustCompile"
op_attrs = {
    "Tin": tin_attr,
    "Tout": tout_attr,
    "f": func_attr,
    "config_proto": config_proto,
    "executor_type": executor_type_attr,
}
if xla_compile_attr in f.definition.attr:
    op_attrs[xla_compile_attr] = f.definition.attr[xla_compile_attr]
op = graph.create_op(op_name, args, tout, name=op_name, attrs=op_attrs)
outputs = op.outputs
if hasattr(f, "graph"):
    _set_read_only_resource_inputs_attr(op, f.graph)
    if hasattr(f.graph, "collective_manager_ids_used"):
        ops.set_int_list_attr(op, acd.COLLECTIVE_MANAGER_IDS,
                              f.graph.collective_manager_ids_used)
exit(outputs if outputs else op)
