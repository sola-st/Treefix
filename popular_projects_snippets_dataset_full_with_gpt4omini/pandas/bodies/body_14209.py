# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
if method in ["to_latex"]:  # uses styler implementation
    pytest.importorskip("jinja2")
msg = "buf is not a file name and it has no write method"
with pytest.raises(TypeError, match=msg):
    getattr(float_frame, method)(buf=object())
