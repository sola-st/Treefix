# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# GH17054

result = self.read_html(
    """
            <table>
                <tr>
                    <td rowspan="3">A</td>
                    <td rowspan="3">B</td>
                </tr>
            </table>
        """,
    header=0,
)[0]

expected = DataFrame(data=[["A", "B"], ["A", "B"]], columns=["A", "B"])

tm.assert_frame_equal(result, expected)
