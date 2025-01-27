# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_test.py
with self.cached_session():
    x = constant_op.constant([[3.]])
    y_nc = math_ops.matmul(x, x, name="not_compiled")
    with jit.experimental_jit_scope():
        y_c = math_ops.matmul(y_nc, y_nc, name="compiled")
    x_grads = gradients.gradients([y_c], [x])[0]
    operations = x.graph.get_operations()
    c_grad_ops = [
        op for op in operations if "gradients/compiled" in op.name]
    nc_grad_ops = [
        op for op in operations if "gradients/not_compiled" in op.name]
    self.assertGreater(len(c_grad_ops), 0)
    self.assertGreater(len(nc_grad_ops), 0)
    for cg in c_grad_ops:
        self.assertTrue(cg.get_attr("_XlaCompile"))
    for ncg in nc_grad_ops:
        with self.assertRaisesRegex(ValueError, "[Nn]o attr named"):
            ncg.get_attr("_XlaCompile")

      # d/dx (x ** 4) = 4 * (x ** 3)
    self.assertAllClose([[108]], x_grads)
