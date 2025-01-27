# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

@api.do_not_convert()
def unconverted_fn():
    self.assertEqual(ag_ctx.control_status_ctx().status,
                     ag_ctx.Status.DISABLED)

@api.convert()
def converted_fn():
    self.assertEqual(ag_ctx.control_status_ctx().status,
                     ag_ctx.Status.ENABLED)
    unconverted_fn()
    self.assertEqual(ag_ctx.control_status_ctx().status,
                     ag_ctx.Status.ENABLED)

self.assertEqual(ag_ctx.control_status_ctx().status,
                 ag_ctx.Status.UNSPECIFIED)
converted_fn()
self.assertEqual(ag_ctx.control_status_ctx().status,
                 ag_ctx.Status.UNSPECIFIED)

@api.call_with_unspecified_conversion_status
def unspecified_fn():
    self.assertEqual(ag_ctx.control_status_ctx().status,
                     ag_ctx.Status.UNSPECIFIED)

unspecified_fn()
