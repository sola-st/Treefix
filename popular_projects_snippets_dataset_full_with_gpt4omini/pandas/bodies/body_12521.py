# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
result = self.read_html(
    """
            <table>
                <tr>
                    <th>A</th>
                    <th>B</th>
                </tr>
                <tr>
                    <td>a</td>
                    <td>b</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                </tr>
            </table>
        """
)[0]

expected = DataFrame(data=[["a", "b"], [np.nan, np.nan]], columns=["A", "B"])

tm.assert_frame_equal(result, expected)
