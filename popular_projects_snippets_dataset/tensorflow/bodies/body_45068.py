# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
self.assertEqual(ag_ctx.control_status_ctx().status,
                 ag_ctx.Status.UNSPECIFIED)
self.assertFalse(converter_testing.is_inside_generated_code())
