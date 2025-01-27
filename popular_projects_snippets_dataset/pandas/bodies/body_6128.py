# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reshaping.py
# GH-33027
a = pd.DataFrame({"a": data[:5]})
b = pd.DataFrame({"b": data[:5]})
result = pd.concat([a, b], ignore_index=True)
expected = pd.DataFrame(
    {
        "a": data.take(list(range(5)) + ([-1] * 5), allow_fill=True),
        "b": data.take(([-1] * 5) + list(range(5)), allow_fill=True),
    }
)
self.assert_frame_equal(result, expected)
