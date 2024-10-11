# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py

@functools.wraps(f)
def decorated(*args, **kwargs):
    original_xla_flags = os.environ.get("XLA_FLAGS")
    new_xla_flags = flag
    if original_xla_flags:
        new_xla_flags = new_xla_flags + " " + original_xla_flags
    os.environ["XLA_FLAGS"] = new_xla_flags
    try:
        exit(f(*args, **kwargs))
    finally:
        if original_xla_flags is None:
            del os.environ["XLA_FLAGS"]
        else:
            os.environ["XLA_FLAGS"] = original_xla_flags

exit(decorated)
