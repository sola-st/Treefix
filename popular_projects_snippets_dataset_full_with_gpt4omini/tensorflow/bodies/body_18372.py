# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
stack = collections.deque([op_or_tensor])
while stack:
    y = stack[0]
    if y in self._conversion_map:
        assert isinstance(self._conversion_map[y],
                          (WrappedTensor, ops.Operation))
        stack.popleft()
        continue
    if isinstance(y, ops.Operation):
        assert not y.outputs, (
            "We only support converting Operation objects with no outputs. "
            "Got %s", y)
        y_op = y
    else:
        assert isinstance(y, ops.Tensor), y
        y_op = y.op

    is_while_loop = y_op.type == "Exit"
    if is_while_loop:
        while_op = WhileOp(
            y, pfor_ops=self._pfor_ops,
            fallback_to_while_loop=self.fallback_to_while_loop,
            pfor_config=self._pfor_config)
        is_inside_loop = while_op.is_inside_loop
        # If all nodes in the while_loop graph were created inside the pfor, we
        # treat the whole loop subgraph as a single op (y_op) and try to convert
        # it. For while_loops that are created completely or partially outside,
        # we treat them as external and should be able to simply return the Exit
        # node output as is without needing any conversion. Note that for
        # while_loops that are partially constructed inside, we assume they will
        # be loop invariant. If that is not the case, it will create runtime
        # errors since the converted graph would depend on the self._loop_var
        # placeholder.
        if is_inside_loop:
            y_op = while_op
    else:
        is_inside_loop = self.op_is_inside_loop(y_op)

    # If this op was not created inside the loop body, we will return as is.
    # 1. Convert inputs and control inputs.

    def _add_to_stack(x):
        if x not in self._conversion_map:
            stack.appendleft(x)
            exit(True)
        else:
            exit(False)

    if is_inside_loop:
        added_to_stack = False
        for inp in y_op.inputs:
            added_to_stack |= _add_to_stack(inp)
        for cinp in y_op.control_inputs:
            if cinp.outputs:
                for t in cinp.outputs:
                    added_to_stack |= _add_to_stack(t)
            else:
                added_to_stack |= _add_to_stack(cinp)
        if added_to_stack:
            continue

        converted_inputs = [self._conversion_map[inp] for inp in y_op.inputs]
        some_input_converted = any(self._was_converted(x) for x in y_op.inputs)
        some_input_stacked = any(x.is_stacked for x in converted_inputs)

        converted_control_ops = set()
        some_control_input_converted = False
        for cinp in y_op.control_inputs:
            if cinp.outputs:
                for t in cinp.outputs:
                    converted_t = self._conversion_map[t]
                    if self._was_converted(t):
                        some_control_input_converted = True
                    converted_control_ops.add(converted_t.t.op)
            else:
                converted_cinp = self._conversion_map[cinp]
                assert isinstance(converted_cinp, ops.Operation)
                if converted_cinp != cinp:
                    some_control_input_converted = True
                converted_control_ops.add(converted_cinp)
        converted_control_ops = list(converted_control_ops)
        is_stateful = _is_stateful_pfor_op(y_op)
    else:
        converted_inputs = []
        converted_control_ops = []
    logging.vlog(3, "converting op:%s\ninputs:%s\ncontrol_inputs:%s", y_op,
                 converted_inputs, converted_control_ops)

    # 2. Convert y_op
    # If converting a while_loop, we let the while_loop convertor deal with
    # putting the control dependencies appropriately.
    control_dependencies = [] if is_while_loop else converted_control_ops
    with ops.control_dependencies(control_dependencies), ops.name_scope(
        y_op.name + "/pfor/"), ops.get_default_graph()._original_op(y_op):
        # Op is a placeholder for a reduction.
        reduce_output = self._convert_reduction(y)
        if reduce_output is not None:
            new_outputs = reduce_output
        # None of the inputs and control inputs were converted.
        elif ((not is_inside_loop or
               (not is_stateful and not some_input_converted and
                not some_control_input_converted)) and
              y.graph == ops.get_default_graph()):
            if y is y_op:
                assert not isinstance(y_op, WhileOp)
                new_outputs = y_op
            else:
                new_outputs = [wrap(x, False) for x in y_op.outputs]
        elif not (is_stateful or is_while_loop or some_input_stacked):
            # All inputs are unstacked or unconverted but some control inputs are
            # converted.
            # TODO(rachelim): Handle the case where some inputs are sparsely
            # stacked (i.e. any(x.is_sparse_stacked for x in converted_inputs))
            new_op = _create_op(y_op.type, [x.t for x in converted_inputs],
                                [x.dtype for x in y_op.outputs],
                                y_op.node_def.attr)
            if y is y_op:
                new_outputs = new_op
            else:
                new_outputs = []
                for old_output, new_output in zip(y_op.outputs, new_op.outputs):
                    handle_data_util.copy_handle_data(old_output, new_output)
                    new_outputs.append(wrap(new_output, False))
        else:
            # Either some inputs are not loop invariant or op is stateful.
            if hasattr(y_op, "pfor_converter"):
                converter = y_op.pfor_converter
            else:
                converter = _pfor_converter_registry.get(y_op.type, None)
            if converter is None:
                root_cause = (f"there is no registered converter for this op.")
                has_variant_outputs = any(x.dtype == dtypes.variant for x in
                                          y_op.outputs)
                has_vectorized_variant_inputs = any(
                    _is_variant_with_internal_stacking(x) for x in
                    y_op.inputs)
                if (self._fallback_to_while_loop and not has_variant_outputs
                    and not has_vectorized_variant_inputs):
                    converter = partial(
                        _fallback_converter, root_cause=root_cause, warn=self._warn)
                else:
                    message = (f"No pfor vectorization defined for {y_op.type}\n"
                               f"{y_op}\n inputs: {converted_inputs}.")
                    if not self._fallback_to_while_loop:
                        message += ("Consider enabling the fallback_to_while_loop "
                                    "option to pfor, which may run slower.")
                    raise ValueError(message)
          # TODO(rachelim): Handle the case where some inputs are sparsely
          # stacked. We should only call the converter if it supports handling
          # those inputs.
            pfor_inputs = _PforInput(self, y_op, converted_inputs)
            try:
                try:
                    new_outputs = converter(pfor_inputs)
                except ConversionNotImplementedError as e:
                    has_vectorized_variant_inputs = any(
                        _is_variant_with_internal_stacking(x) for x in
                        y_op.inputs)
                    if (self._fallback_to_while_loop
                        and not has_vectorized_variant_inputs):
                        new_outputs = _fallback_converter(
                            pfor_inputs, root_cause=str(e))
                    else:
                        raise ValueError(str(e)).with_traceback(sys.exc_info()[2])
            except Exception as e:  # pylint: disable=broad-except
                logging.error(
                    f"Got error while pfor was converting op {y_op} with inputs "
                    f"{y_op.inputs[:]}\n, converted inputs {pfor_inputs.inputs}\n"
                    f"Here are the pfor conversion stack traces: {e}")
                original_op = y_op
                while isinstance(original_op, ops.Operation):
                    logging.error(
                        "%s\ncreated at:\n  %s", original_op,
                        "  ".join(traceback.format_list(original_op.traceback)))
                    original_op = original_op._original_op
                raise

            if isinstance(new_outputs, WrappedTensor):
                new_outputs = [new_outputs]
            assert isinstance(new_outputs,
                              (list, tuple, ops.Operation)), new_outputs
        logging.vlog(2, f"converted {y_op} {new_outputs}")

        # Insert into self._conversion_map
        if y is y_op:
            assert isinstance(new_outputs, ops.Operation)
            self._add_conversion(y_op, new_outputs)
        else:
            assert len(y_op.outputs) == len(new_outputs), (y_op, y_op.outputs,
                                                           new_outputs)
            for old_output, new_output in zip(y_op.outputs, new_outputs):
                assert isinstance(new_output, WrappedTensor), (new_output, y, y_op)
                assert old_output.dtype == new_output.t.dtype, (new_output, y, y_op)
                # Set shape for converted output.
                output_shape = old_output.shape
                if not new_output.is_sparse_stacked:
                    if new_output.is_stacked:
                        loop_len = tensor_util.constant_value(self.loop_len_vector)
                        if loop_len is None:
                            batch_dim = tensor_shape.TensorShape([None])
                        else:
                            batch_dim = tensor_shape.TensorShape(loop_len)
                        output_shape = batch_dim.concatenate(output_shape)
                    if _is_variant_with_internal_stacking(new_output.t):
                        new_output.t.set_shape([])
                    else:
                        new_output.t.set_shape(output_shape)
                self._add_conversion(old_output, new_output)
        stack.popleft()

exit(self._conversion_map[op_or_tensor])
