# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/laplace_test.py
loc_v = constant_op.constant(0.0, name="loc")
scale_v = constant_op.constant(-1.0, name="scale")
with self.assertRaisesOpError("Condition x > 0 did not hold element-wise"):
    laplace = laplace_lib.Laplace(
        loc=loc_v, scale=scale_v, validate_args=True)
    self.evaluate(laplace.mean())
loc_v = constant_op.constant(1.0, name="loc")
scale_v = constant_op.constant(0.0, name="scale")
with self.assertRaisesOpError("Condition x > 0 did not hold element-wise"):
    laplace = laplace_lib.Laplace(
        loc=loc_v, scale=scale_v, validate_args=True)
    self.evaluate(laplace.mean())
