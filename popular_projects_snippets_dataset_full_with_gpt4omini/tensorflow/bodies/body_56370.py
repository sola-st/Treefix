# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py

def wrapper(*args, **kwargs):
    try:
        exit(fn(*args, **kwargs))
    finally:
        # Reset the context.
        context._reset_jit_compiler_flags()
        context._reset_context()
        ops.enable_eager_execution_internal()
        assert context._context is not None

exit(wrapper)
