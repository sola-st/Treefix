# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Builds graph operators that runs compilation and replicated computation.

  This is a lower level interface than replicate that returns a separate compile
  and execute output tensor. In the generated graph the compile op feeds into
  the execute op and no additional compilation is incurred when running the
  compile op before the execute op. The compile op returns additional
  information about the compilation but does not return the compiled program.

  Args:
    computation: A Python function that builds the computation to replicate.
    inputs: A list of lists of input tensors or `None` (equivalent to
      `[[]]`), indexed by `[replica_num][input_num]`. All replicas must
      have the same number of inputs. Each input can be a nested structure
      containing values that are convertible to tensors. Note that passing an
      N-dimension list of compatible values will result in a N-dimension list of
      scalar tensors rather than a single Rank-N tensors. If you need different
      behavior, convert part of inputs to tensors with `tf.convert_to_tensor`.
    infeed_queue: If not `None`, the `InfeedQueue` from which to append a tuple
      of arguments as inputs to computation.
    device_assignment: If not `None`, a `DeviceAssignment` describing the
      mapping between logical cores in the computation with physical cores in
      the TPU topology. Uses a default device assignment if `None`. The
      `DeviceAssignment` may be omitted if each replica of the computation uses
      only one core, and there is either only one replica, or the number of
      replicas is equal to the number of cores in the TPU system.
    name: (Deprecated) Does nothing.
    use_tpu: When false, the input `computation` is executed on the XLA CPU/GPU
      backends. Currently, only supports a default placement (computation is
      placed on GPU if one is available, and on CPU if not).
    maximum_shapes: A nested structure of tf.TensorShape representing the shape
      to which the respective component of each input element in each replica
      should be padded. Any unknown dimensions (e.g.
      tf.compat.v1.Dimension(None) in a tf.TensorShape or -1 in a tensor-like
      object) will be padded to the maximum size of that dimension over all
      replicas. The structure of `maximum_shapes` needs to be the same as
      `inputs[0]`.
    padding_spec: An enum specified by `tf.tpu.PaddingSpec`. This describes the
      padding policy when the `inputs` to `tf.tpu.replicate` is dynamic.
      One usage is to enable automatic bucketizing on the inputs by setting the
      value to `tpu.PaddingSpec.POWER_OF_TWO`, which can help to reduce the
      recompilation in the XLA side.
    xla_options: An instance of `tpu.XLAOptions` which indicates the options
      passed to XLA compiler. Use `None` for default options.

  Returns:
    A list of lists with the first list corresponding to the compile op and the
    second a list of output tensors, indexed by `[replica_num][output_num]`.
  Raises:
    ValueError: If all replicas do not have equal numbers of input tensors.
    ValueError: If the number of inputs per replica does not match
      the number of formal parameters to `computation`.
    ValueError: If the static `inputs` dimensions don't match with the values
      given in `maximum_shapes`.
    ValueError: If the structure of inputs per replica does not match
      the structure of `maximum_shapes`.
  """
del name
inputs = [[]] if inputs is None else inputs
xla_options = xla_options or XLAOptions()

metadata_kwargs = {}
if device_assignment is not None:
    # Turn the Numpy array into a flattened list so we can pass it as an
    # operator attribute.
    metadata_kwargs = {
        "topology":
            device_assignment.topology.serialized(),
        "device_assignment":
            device_assignment.core_assignment.flatten().tolist()
    }
    metadata_kwargs["num_cores_per_replica"] = (
        device_assignment.num_cores_per_replica)

# This entry is used for enabling automatic outside compilation.
metadata_kwargs["allow_soft_placement"] = config.get_soft_device_placement()
if config.get_soft_device_placement():
    logging.info("Automatic outside compilation is enabled. "
                 "Ops without XLA kernels will be automatically "
                 "placed on CPU.")

if not isinstance(inputs, list):
    raise TypeError("tpu.replicate() inputs must be a list of lists/tuples, "
                    f"received {type(inputs)}")
if any(not isinstance(inp, (list, tuple)) for inp in inputs):
    raise TypeError(
        "tpu.replicate() inputs must be a list of lists/tuples, "
        f"received types: {[type(inp) for inp in inputs]}")

num_replicas = len(inputs)

# No replicas? Nothing to do.
if num_replicas == 0:
    exit([])

# Checks all replicas have the same structure.
for i in range(1, num_replicas):
    nest.assert_same_structure(inputs[0], inputs[i])

# Explicitly read variables.
inputs = variable_utils.convert_variables_to_tensors(inputs)
# Flatten inputs. This structure may contain None values, which will be
# handled later.
flat_inputs_with_nones = [
    nest.flatten(per_replica_input, expand_composites=True)
    for per_replica_input in inputs
]
# Mask parallel to one replica's inputs with True for tensors coming from
# composites.
is_composite = nest.flatten(nest.map_structure(
    lambda x: _flatten_and_filter_composite(x, False, True), inputs[0]))

# Converts inputs to Tensors, replacing Nones with a placeholder 0 since
# tpu_ops.tpu_replicated_input() can't handle non-Tensor values.
flat_inputs = []
for inp in flat_inputs_with_nones:
    flat_inputs.append([
        constant_op.constant(0) if x is None else ops.convert_to_tensor(x)
        for x in inp
    ])

# Verifies that all replicas have matching numbers and types of inputs
flat_input_types = [x.dtype for x in flat_inputs[0]]
input_arity = len(inputs[0])
flat_input_arity = len(flat_input_types)
for i in range(num_replicas):
    if len(inputs[i]) != input_arity:
        raise ValueError("Replicas must have the same number of inputs. "
                         "Replica 0 had {} inputs, replica {} had {} "
                         "inputs.".format(input_arity, i, len(inputs[i])))

    types = [x.dtype for x in flat_inputs[i]]
    if types != flat_input_types:
        raise ValueError("Replicas must have matching input types. Replica 0 had "
                         "input types {}, replica {} had input types {}".format(
                             flat_input_types, i, types))

arg_error = xla.check_function_argument_count(
    computation, input_arity, infeed_queue)
if arg_error is not None:
    if infeed_queue is None:
        raise TypeError(
            "Supplied computation cannot be called with the specified inputs. "
            f"You specified {input_arity} inputs: {[i.name for i in inputs[0]]}, "
            f"but the computation needs {arg_error}")
    else:
        raise TypeError(
            "Supplied computation cannot be called with the specified inputs. "
            f"You specified {input_arity} inputs: {[i.name for i in inputs[0]]} ",
            f"and {infeed_queue.number_of_tuple_elements} additional inputs "
            f"from infeed, but the computation needs {arg_error}")

dynamic_shape_inputs = False
if maximum_shapes:
    if infeed_queue:
        raise ValueError(
            "Dynamic input shapes are not supported with infeed queues")

    # Make sure maximum_shapes has the same structure as inputs.
    nest.assert_same_structure(inputs[0], maximum_shapes, check_types=False)

    # Flatten padded shapes:
    # For composite tensor components, we don't want to pad them. For each
    # entry of maximum_shapes that corresponds to a composite tensor, replace it
    # by a tuple of Nones of the same length as the number of components of the
    # composite tensor. When we flatten a second time, this makes
    # flat_maximum_shapes have the same length as flat_inputs[i]. We can then
    # avoid padding these tensors. The assumption is that they will be used by
    # outside compilation or that the components are statically shaped and will
    # be used by tpu compatible ops.
    flat_maximum_shapes = nest.flatten(
        [_flatten_and_filter_composite(x, y)
         for x, y in zip(nest.flatten(inputs[0]),
                         nest.flatten(maximum_shapes))])
    flat_maximum_shapes = [
        tensor_shape.TensorShape(s) if s is not None else None
        for s in flat_maximum_shapes
    ]
    nest.assert_same_structure(flat_inputs[0], flat_maximum_shapes,
                               check_types=False)

    unpadded_inputs = flat_inputs
    flat_inputs, padding_maps = _pad_all_input(unpadded_inputs,
                                               flat_maximum_shapes,
                                               padding_spec)
    if padding_maps:
        dynamic_shape_inputs = True
        logging.info("TPU has inputs with dynamic shapes: %s", inputs[0])

metadata_kwargs["step_marker_location"] = getattr(
    computation, "step_marker_location", "STEP_MARK_AT_ENTRY")
metadata_kwargs["use_spmd_for_xla_partitioning"] = \
      xla_options.use_spmd_for_xla_partitioning

graph = ops.get_default_graph()

# Fan-in: Builds a TPUReplicatedInput node for each input.
flat_replicated_inputs = []
for i in range(0, len(flat_inputs[0])):
    replicas = [flat_inputs[replica][i] for replica in range(num_replicas)]
    flat_replicated_inputs.append(
        tpu_ops.tpu_replicated_input(
            replicas, name="input{}".format(i)))
if isinstance(graph, func_graph.FuncGraph):
    # When we are in Tensorflow 2.0 function, 'graph' will be a FuncGraph
    # object. If both outside graph and this function have a TPU cluster,
    # they will have the same cluster name and it will cause problems (because
    # we lower functional ops in Tensorflow 2.0). Append function name to
    # 'cluster_name' to avoid cluster name collision.
    cluster_name = graph.unique_name("cluster_" + graph.name)
else:
    cluster_name = graph.unique_name("cluster")
pivot = control_flow_ops.no_op(name=cluster_name + "/pivot")
pivot._set_attr(_PIVOT_FOR_CLUSTER,  # pylint: disable=protected-access
                attr_value_pb2.AttrValue(s=compat.as_bytes(cluster_name)))
context = TPUReplicateContext(
    name=cluster_name, num_replicas=num_replicas, pivot=pivot)
try:
    context.Enter()

    metadata = tpu_ops.tpu_replicate_metadata(
        num_replicas=num_replicas, use_tpu=use_tpu, **metadata_kwargs)

    with tpu_function.tpu_shard_context(
        num_replicas), ops.control_dependencies([metadata]):

        if dynamic_shape_inputs and xla_options.enable_xla_dynamic_padder:
            for padding_map in padding_maps:
                input_shape = flat_replicated_inputs[padding_map.arg_index].shape
                flat_replicated_inputs[
                    padding_map.arg_index] = tf2xla.set_dynamic_dimension_size(
                        flat_replicated_inputs[padding_map.arg_index],
                        padding_map.shape_index,
                        flat_replicated_inputs[padding_map.padding_arg_index])
                flat_replicated_inputs[padding_map.arg_index].set_shape(input_shape)

      # Add identity ops so even unused inputs are "consumed" by the
      # computation. This is to avoid orphaned TPUReplicatedInput nodes.
      # TODO(phawkins): consider instead pruning unused TPUReplicatedInput
      # and eliding trivial TPUReplicatedInput/TPUReplicatedOutput pairs.
        flat_replicated_inputs = [
            array_ops.identity(x, name="replicated_input_{}".format(i))
            for i, x in enumerate(flat_replicated_inputs)
        ]
        for i, composite in zip(flat_replicated_inputs, is_composite):
            # pylint: disable=protected-access
            # Add an attribute to the identity node so that they could be removed in
            # encapsulate TPU computation pass if unused. However we don't remove
            # inputs when dynamic padding is enabled.
            # TODO(rxsang): Use other ways except argument index in padding_map so
            # outside compilation can work with dynamic padding correctly.
            if not dynamic_shape_inputs or composite:
                i.op._set_attr("_tpu_input_identity",
                               attr_value_pb2.AttrValue(b=True))
            # pylint: enable=protected-access

      # Clobber replicated placeholders with Nones.
        computation_inputs = [
            None if inp is None else replicated for replicated, inp in zip(
                flat_replicated_inputs, flat_inputs_with_nones[0])
        ]

        # Unflatten the computation inputs to match original input structure.
        computation_inputs = nest.pack_sequence_as(
            structure=inputs[0],
            flat_sequence=computation_inputs[:flat_input_arity],
            expand_composites=True)

        # If there is an infeed queue, adds the dequeued values to the
        # computation's inputs.
        if infeed_queue is not None:
            infeed_queue.set_number_of_shards(num_replicas)
            for t in infeed_queue.generate_dequeue_op():
                computation_inputs.append(t)

      # Only resource variables work inside a TPU computation, so turn on
      # resource variables for the computation.
      # TODO(phawkins): consider removing this code. It will
      # be less confusing to clients if they knowingly choose to use resource
      # variables.
      # Partitioned variables is not supported (b/112311320).
        vscope = variable_scope.get_variable_scope()
        saved_use_resource = vscope.use_resource
        saved_custom_getter = vscope.custom_getter

        def custom_getter(getter, name, *args, **kwargs):
            """Variables on TPU have a few restrictions."""
            partitioner = kwargs.get("partitioner", None)
            if partitioner is not None:
                kwargs["partitioner"] = None
                logging.warning(
                    "Partitioned variables are not supported on TPU. Got "
                    "`partitioner` that is %s for variable %s. "
                    "Setting `partitioner` to `None`.", partitioner, name)
            if saved_custom_getter is None:
                exit(getter(name, *args, **kwargs))
            else:
                exit(saved_custom_getter(getter, name, *args, **kwargs))

        vscope.set_use_resource(True)
        vscope.set_custom_getter(custom_getter)

        outputs = computation(*computation_inputs)

        vscope.set_use_resource(saved_use_resource)
        vscope.set_custom_getter(saved_custom_getter)

        outputs = variable_utils.convert_variables_to_tensors(outputs)

    need_spmd_partitioning = (
        xla_options.use_spmd_for_xla_partitioning and
        device_assignment is not None and
        device_assignment.num_cores_per_replica > 1)
    outputs_is_flat = xla.is_flat(outputs)
    if outputs_is_flat:
        output_tensors, control_deps, pack_template = _postprocess_flat_outputs(
            outputs, need_spmd_partitioning)
    else:
        output_tensors, control_deps, pack_template = (
            _postprocess_non_flat_outputs(outputs, need_spmd_partitioning))

    # tensor_tracer imports tpu.py. Local import to tensor_tracer to avoid
    # import-cycle
    if typing.TYPE_CHECKING:
        tensor_tracer = Any
    else:
        # pylint: disable=g-import-not-at-top
        from tensorflow.python.tpu import tensor_tracer
        # pylint: enable=g-import-not-at-top
    if tensor_tracer.TensorTracer.is_enabled():
        if tf2.enabled():
            logging.warn("TF API ver >= 2.0 detected. "
                         "Tensor Tracer v1 is not enabled.")
        else:
            tt = tensor_tracer.TensorTracer()
            output_tensors = tt.trace_tpu(ops.get_default_graph(),
                                          output_tensors, control_deps,
                                          num_replicas)

    context.ExitResult(output_tensors)
finally:
    context.report_unsupported_operations()
    context.Exit()
    host_compute_core = context.HostComputeCore()

if host_compute_core:
    attr_value = attr_value_pb2.AttrValue()
    attr_value.list.s.extend(compat.as_bytes(x) for x in host_compute_core)
    metadata._set_attr("host_compute_core", attr_value)  # pylint: disable=protected-access

with ops.control_dependencies([metadata]):
    if use_tpu:
        compile_status = tpu_ops.tpu_compilation_result()
        op = compile_status.op
        attr_value = attr_value_pb2.AttrValue(s=compat.as_bytes(cluster_name))
        op._set_attr(_TPU_COMPILATION_STATUS_ATTR, attr_value)  # pylint: disable=protected-access
    else:
        compile_status = control_flow_ops.no_op(name="compilation_status")

if not output_tensors:
    # Returns a list of NoOps dependent on the replication Op, indexed by
    # [replica_num].
    exit([
        compile_status,
        [
            control_flow_ops.group(control_deps, name="shard_%d" % i)
            for i in range(num_replicas)
        ]
    ])

# Fan-out: Builds a TPUReplicatedOutput node for each output.
replicated_outputs = [[] for i in range(num_replicas)]
for i, t in enumerate(output_tensors):

    # None values returned by the computation can't be sent to
    # tpu_ops.tpu_replicated_output(), we handle them specially here. We can
    # avoid the placeholder 0 routine required on the inputs since outputs are
    # replicated per-tensor, not per-replica, so we can skip replication.
    if t is None:
        for replica in range(num_replicas):
            replicated_outputs[replica].append(None)
        continue

    # Fan-out: Builds a TPUReplicatedOutput node for each output.
    ys = tpu_ops.tpu_replicated_output(
        t, num_replicas, name="output{}".format(i))

    # Wraps the outputs in identity operators so the names of any possible
    # `fetch` nodes are preserved by the replication rewrite.
    with ops.control_dependencies(control_deps):
        for replica in range(num_replicas):
            replicated_outputs[replica].append(
                array_ops.identity(
                    ys[replica], name="output_%d_shard_%d" % (i, replica)))

replicated_outputs = [
    nest.pack_sequence_as(pack_template, replica_outs, expand_composites=True)
    for replica_outs in replicated_outputs
]

exit([compile_status, replicated_outputs])
