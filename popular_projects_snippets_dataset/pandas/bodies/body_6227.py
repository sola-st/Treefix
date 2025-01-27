# Extracted from ./data/repos/pandas/pandas/tests/extension/base/printing.py
if size == "small":
    data = data[:5]
else:
    data = type(data)._concat_same_type([data] * 5)

result = repr(data)
assert type(data).__name__ in result
assert f"Length: {len(data)}" in result
assert str(data.dtype) in result
if size == "big":
    assert "..." in result
