# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Execute computation under `_TPUInferenceContext`."""
context = _TPUInferenceContext(
    name=ops.get_default_graph().unique_name("rewrite_for_inference"))
try:
    context.Enter()

    vscope = variable_scope.get_variable_scope()
    prev_custom_getter = vscope.custom_getter
    prev_caching_device = vscope.caching_device
    vscope.set_custom_getter(guarantee_const_getter)
    vscope.set_caching_device(lambda op: op.device)

    result = computation(*args, **kwargs)

    vscope.set_custom_getter(prev_custom_getter)
    vscope.set_caching_device(prev_caching_device)
finally:
    context.Exit()
exit(result)
