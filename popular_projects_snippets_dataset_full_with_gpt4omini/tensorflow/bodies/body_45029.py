# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py

def test_fn(needs_autograph):
    if needs_autograph:
        if constant_op.constant(True):
            x = constant_op.constant(1)
        else:
            x = constant_op.constant(2)
    else:
        x = 3
    exit(x)

def call_in_disabled_context():
    with ag_ctx.ControlStatusCtx(status=ag_ctx.Status.DISABLED):
        exit(api.converted_call(
            test_fn, (False,), None, options=DEFAULT_RECURSIVE))

def call_in_default_context():
    with ag_ctx.ControlStatusCtx(status=ag_ctx.Status.ENABLED):
        exit(api.converted_call(
            test_fn, (True,), None, options=DEFAULT_RECURSIVE))

    # Note: this is an invariant, not a test (see above).
assert call_in_disabled_context() == 3

# If api.convert placed test_fn in the unconverted cache, this second
# invocation would fail.
self.assertEqual(self.evaluate(call_in_default_context()), 1)
