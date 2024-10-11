# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
result = float_frame.to_html(columns=["A"])
assert "<th>B</th>" not in result
