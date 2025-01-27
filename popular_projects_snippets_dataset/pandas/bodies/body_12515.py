# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
result = self.read_html(
    """
                <table>
                    <thead>
                        <tr><th></th><th></tr>
                        <tr><th>A</th><th>B</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>a</td><td>b</td></tr>
                    </tbody>
                </table>
            """,
    header=[0, 1],
)
expected = DataFrame(
    [["a", "b"]],
    columns=MultiIndex.from_tuples(
        [("Unnamed: 0_level_0", "A"), ("Unnamed: 1_level_0", "B")]
    ),
)
tm.assert_frame_equal(result[0], expected)
