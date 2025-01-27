# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# GH17054

# In ASCII, with lowercase letters being copies:
#
# A B b b C
# a b b b D

result = self.read_html(
    """
            <table>
                <tr>
                    <td rowspan="2">A</td>
                    <td rowspan="2" colspan="3">B</td>
                    <td>C</td>
                </tr>
                <tr>
                    <td>D</td>
                </tr>
            </table>
        """,
    header=0,
)[0]

expected = DataFrame(
    data=[["A", "B", "B", "B", "D"]], columns=["A", "B", "B.1", "B.2", "C"]
)

tm.assert_frame_equal(result, expected)
