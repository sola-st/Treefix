# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
with option_context("display.max_rows", 60):

    max_rows = get_option("display.max_rows")
    h = max_rows - 1
    df = DataFrame(
        {
            "idx": np.linspace(-10, 10, h),
            "A": np.arange(1, 1 + h),
            "B": np.arange(41, 41 + h),
        }
    ).set_index("idx")
    reg_repr = df._repr_html_()
    assert ".." not in reg_repr
    assert f"<td>{40 + h}</td>" in reg_repr

    h = max_rows + 1
    df = DataFrame(
        {
            "idx": np.linspace(-10, 10, h),
            "A": np.arange(1, 1 + h),
            "B": np.arange(41, 41 + h),
        }
    ).set_index("idx")
    long_repr = df._repr_html_()
    assert ".." in long_repr
    assert "<td>31</td>" not in long_repr
    assert f"{h} rows " in long_repr
    assert "2 columns" in long_repr
