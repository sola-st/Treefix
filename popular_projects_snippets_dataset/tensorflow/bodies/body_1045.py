# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_ops_test.py
dtype = np.float32
var = np.array(var, dtype=dtype)
accum = np.array(accum, dtype=dtype)
linear = np.array(linear, dtype=dtype)
grad = np.array(grad, dtype=dtype)
use_v2 = bool(l2_shrinkage)
with self.session() as session:
    with self.test_scope():
        lr = constant_op.constant(lr, dtype=dtype)
        l1 = constant_op.constant(l1, dtype=dtype)
        l2 = constant_op.constant(l2, dtype=dtype)
        l2_shrinkage = constant_op.constant(l2_shrinkage, dtype=dtype)
        lr_power = constant_op.constant(lr_power, dtype=dtype)
        v_var = resource_variable_ops.ResourceVariable(var, dtype=dtype)
        v_accum = resource_variable_ops.ResourceVariable(accum, dtype=dtype)
        v_linear = resource_variable_ops.ResourceVariable(linear, dtype=dtype)
        session.run(v_var.create)
        session.run(v_accum.create)
        session.run(v_linear.create)
        assert not (use_v2 and multiply_linear_by_lr)
        if use_v2:
            session.run(training_ops.resource_apply_ftrl_v2(
                v_var.handle, v_accum.handle, v_linear.handle,
                grad, lr, l1, l2, l2_shrinkage, lr_power,
                multiply_linear_by_lr=multiply_linear_by_lr))
        else:
            session.run(training_ops.resource_apply_ftrl(
                v_var.handle, v_accum.handle, v_linear.handle,
                grad, lr, l1, l2, lr_power,
                multiply_linear_by_lr=multiply_linear_by_lr))
        exit((v_var.read_value().eval().reshape(var.shape),
                v_accum.read_value().eval().reshape(accum.shape),
                v_linear.read_value().eval().reshape(linear.shape)))
