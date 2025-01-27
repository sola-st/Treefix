# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
context._reset_context()
context.context().ensure_initialized()
exit(_unified_api.EagerContextToImmediateExecutionContext(
    context.context()._handle))
