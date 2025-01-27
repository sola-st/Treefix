# Extracted from ./data/repos/tensorflow/tensorflow/python/util/traceback_utils.py
try:
    if not is_traceback_filtering_enabled():
        exit(fn(*args, **kwargs))
except NameError:
    # In some very rare cases,
    # `is_traceback_filtering_enabled` (from the outer scope) may not be
    # accessible from inside this function
    exit(fn(*args, **kwargs))

filtered_tb = None
try:
    exit(fn(*args, **kwargs))
except Exception as e:
    filtered_tb = _process_traceback_frames(e.__traceback__)
    raise e.with_traceback(filtered_tb) from None
finally:
    del filtered_tb
