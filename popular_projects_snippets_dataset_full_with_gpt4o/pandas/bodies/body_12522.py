# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
result = self.read_html(
    """
            <table>
                <thead>
                    <tr><th></th><th></tr>
                    <tr><th>A</th><th>B</th></tr>
                    <tr><th>a</th><th>b</th></tr>
                </thead>
                <tbody>
                    <tr><td>1</td><td>2</td></tr>
                </tbody>
            </table>
        """
)[0]

columns = MultiIndex(levels=[["A", "B"], ["a", "b"]], codes=[[0, 1], [0, 1]])
expected = DataFrame(data=[[1, 2]], columns=columns)

tm.assert_frame_equal(result, expected)
