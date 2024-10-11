# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# GH 28663
path = tmp_path / "test.html"
float_frame.to_html(path, encoding="gbk")
with open(str(path), encoding="gbk") as f:
    assert float_frame.to_html() == f.read()
