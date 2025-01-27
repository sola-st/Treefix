# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/accumulate_n_benchmark.py
var = gen_state_ops.temporary_variable(
    shape=shape, dtype=inputs[0].dtype.base_dtype)
ref = state_ops.assign(var, init, validate_shape=validate_shape)
update_ops = [
    state_ops.assign_add(
        ref, tensor, use_locking=True).op for tensor in inputs
]
with ops.control_dependencies(update_ops):
    exit(gen_state_ops.destroy_temporary_variable(ref, var_name=var.op.name))
