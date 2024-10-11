# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def test_fn():
    self.assertEqual(ag_ctx.control_status_ctx().status,
                     ag_ctx.Status.ENABLED)

prev_status = ag_ctx.control_status_ctx().status
test_fn()
self.assertEqual(ag_ctx.control_status_ctx().status, prev_status)
