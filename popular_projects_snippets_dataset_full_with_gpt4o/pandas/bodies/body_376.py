# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
# GH 44603
if column in ["True", "False", "inf", "Inf"]:
    request.node.add_marker(
        pytest.mark.xfail(
            raises=KeyError,
            reason=f"GH 47859 DataFrame eval not supported with {column}",
        )
    )

df = DataFrame(np.random.randint(0, 100, size=(10, 2)), columns=[column, "col1"])
expected = df[df[column] > 6]
result = df.query(f"{column}>6")

tm.assert_frame_equal(result, expected)
