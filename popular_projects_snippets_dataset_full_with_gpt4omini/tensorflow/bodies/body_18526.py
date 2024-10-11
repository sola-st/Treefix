# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
if indices is None:
    indices = pfor_input.pfor.all_indices
    partitioned = pfor_input.pfor.all_indices_partitioned
else:
    partitioned = True
func = pfor_input.op.graph._get_function(func_name)
converter = PFor(
    loop_var=pfor_input.pfor.loop_var,
    loop_len=array_ops.size(indices),
    pfor_ops=func.graph.get_operations(),
    fallback_to_while_loop=pfor_input.pfor.fallback_to_while_loop,
    all_indices=indices,
    all_indices_partitioned=partitioned,
    pfor_config=pfor_input.pfor.pfor_config)
outputs = _convert_function_call(func, converter, inputs)
stacked_outputs = []
for out in outputs:
    if not out.is_stacked:
        stacked_outputs.append(_stack(out.t, [array_ops.size(indices)]).t)
    else:
        stacked_outputs.append(out.t)
exit(stacked_outputs)
