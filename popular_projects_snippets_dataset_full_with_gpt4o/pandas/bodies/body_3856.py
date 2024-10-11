# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
buf = StringIO()

# mixed
repr(float_string_frame)
float_string_frame.info(verbose=False, buf=buf)
