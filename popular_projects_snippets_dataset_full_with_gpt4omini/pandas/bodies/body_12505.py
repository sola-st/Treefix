# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# GH17054
result = self.read_html(
    """
            <table>
                <tr>
                    <th>A</th>
                    <th colspan="1">B</th>
                    <th rowspan="1">C</th>
                </tr>
                <tr>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                </tr>
            </table>
        """
)[0]

expected = DataFrame([["a", "b", "c"]], columns=["A", "B", "C"])

tm.assert_frame_equal(result, expected)
