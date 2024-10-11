# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# GH17054

# In ASCII, with lowercase letters being copies:
#
# X x Y Z W
# A B b z C

result = self.read_html(
    """
            <table>
                <tr>
                    <td colspan="2">X</td>
                    <td>Y</td>
                    <td rowspan="2">Z</td>
                    <td>W</td>
                </tr>
                <tr>
                    <td>A</td>
                    <td colspan="2">B</td>
                    <td>C</td>
                </tr>
            </table>
        """,
    header=0,
)[0]

expected = DataFrame(
    data=[["A", "B", "B", "Z", "C"]], columns=["X", "X.1", "Y", "Z", "W"]
)

tm.assert_frame_equal(result, expected)
