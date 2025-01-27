# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_quantile.py
if interpolation == "nearest" and q == 0.5 and b_vals == [4, 3, 2, 1]:
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Unclear numpy expectation for nearest "
            "result with equidistant data"
        )
    )

a_expected = pd.Series(a_vals).quantile(q, interpolation=interpolation)
b_expected = pd.Series(b_vals).quantile(q, interpolation=interpolation)

df = DataFrame(
    {"key": ["a"] * len(a_vals) + ["b"] * len(b_vals), "val": a_vals + b_vals}
)

expected = DataFrame(
    [a_expected, b_expected], columns=["val"], index=Index(["a", "b"], name="key")
)
result = df.groupby("key").quantile(q, interpolation=interpolation)

tm.assert_frame_equal(result, expected)
