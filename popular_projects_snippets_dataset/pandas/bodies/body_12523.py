# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# Issue #13434
expected_df = DataFrame(
    data=[("Hillary", 68, "D"), ("Bernie", 74, "D"), ("Donald", 69, "R")]
)
expected_df.columns = [
    ["Unnamed: 0_level_0", "Age", "Party"],
    ["Name", "Unnamed: 1_level_1", "Unnamed: 2_level_1"],
]
html = expected_df.to_html(index=False)
html_df = self.read_html(html)[0]
tm.assert_frame_equal(expected_df, html_df)
