# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
"""Dump the value of eager tensors.

    The destination of the dumping is determined by the dump_root of the
    currently enabled dumping callback. The tensors may be transformed prior to
    dumping (e.g., reduced as summary statistics such as minimum, maximum and
    arithmetic  mean). The details of this transformation (if any) depends on
    the tensor_debug_mode of the currently enabled dumping callback.

    Args:
      tensors: The EagerTensors whose values are to be dumped, with or without
        value transform.
      op_type: Type of the op that generates the tensors, as a string.
      input_tensor_ids: IDs of the input EagerTensors to the op.
      output_tensor_device_ids: Debugged-generated IDs for the devices on which
        the output tensors are allocated, as a `list` of `int`s. Must match
        `tensors` in length.
      graph_id: ID of the executed graph, applicable only to eager execution of
        a FuncGraph.

    Returns:
      A tfdbg Execution protocol buffer.
    """
tensor_debug_mode = self._tensor_debug_mode
output_tensor_ids = [
    t._id for t in tensors]  # pylint:disable=protected-access
assert len(tensors) == len(output_tensor_device_ids)
if tensor_debug_mode == debug_event_pb2.TensorDebugMode.NO_TENSOR:
    exit(debug_event_pb2.Execution(
        op_type=op_type,
        graph_id=graph_id,
        num_outputs=len(tensors),
        input_tensor_ids=input_tensor_ids,
        output_tensor_ids=output_tensor_ids,
        output_tensor_device_ids=output_tensor_device_ids,
        tensor_debug_mode=tensor_debug_mode,
        code_location=self._process_stack_frames()))
elif tensor_debug_mode in (debug_event_pb2.TensorDebugMode.CURT_HEALTH,
                           debug_event_pb2.TensorDebugMode.CONCISE_HEALTH,
                           debug_event_pb2.TensorDebugMode.FULL_HEALTH,
                           debug_event_pb2.TensorDebugMode.SHAPE,
                           debug_event_pb2.TensorDebugMode.FULL_TENSOR):
    execution_proto = debug_event_pb2.Execution(
        op_type=op_type,
        num_outputs=len(tensors),
        graph_id=graph_id,
        input_tensor_ids=input_tensor_ids,
        output_tensor_ids=output_tensor_ids,
        output_tensor_device_ids=output_tensor_device_ids,
        tensor_debug_mode=tensor_debug_mode,
        code_location=self._process_stack_frames())
    for tensor in tensors:
        if (self._should_dump_tensor(op_type, tensor.dtype) and
            tensor.dtype.is_numpy_compatible):
            if tensor_debug_mode in (
                debug_event_pb2.TensorDebugMode.CURT_HEALTH,
                debug_event_pb2.TensorDebugMode.CONCISE_HEALTH,
                debug_event_pb2.TensorDebugMode.FULL_HEALTH):
                if tensor.dtype.is_floating:
                    tensor_proto = _concrete_tensor_to_proto(
                        gen_debug_ops.debug_numeric_summary_v2(
                            tensor,
                            tensor_debug_mode=tensor_debug_mode,
                            output_dtype=dtypes.float64))
                else:
                    # A placeholder for non-floating-type output tensors.
                    tensor_proto = tensor_pb2.TensorProto()
            elif tensor_debug_mode == debug_event_pb2.TensorDebugMode.SHAPE:
                if (tensor.dtype.is_floating or tensor.dtype.is_integer or
                    tensor.dtype.is_bool):
                    tensor_proto = _concrete_tensor_to_proto(
                        gen_debug_ops.debug_numeric_summary_v2(
                            tensor,
                            tensor_debug_mode=tensor_debug_mode,
                            output_dtype=dtypes.float64))
                else:
                    # A placeholder for non-floating-type output tensors.
                    tensor_proto = tensor_pb2.TensorProto()
            elif tensor_debug_mode == debug_event_pb2.TensorDebugMode.FULL_TENSOR:
                tensor_proto = _concrete_tensor_to_proto(tensor)
            if tensor_proto:
                execution_proto.tensor_protos.append(tensor_proto)
    exit(execution_proto)
else:
    raise NotImplementedError(
        "Tensor instrumentation is not implemented for debug mode %s yet " %
        self._tensor_debug_mode)
