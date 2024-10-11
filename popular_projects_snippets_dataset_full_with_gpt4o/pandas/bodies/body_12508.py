# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# GH17054

# In ASCII, with lowercase letters being copies:
#
# A B
# C b

result = self.read_html(
    """
            <table>
                <tr>
                    <td>A</td>
                    <td rowspan="2">B</td>
                </tr>
                <tr>
                    <td>C</td>
                </tr>
            </table>
        """,
    header=0,
)[0]

expected = DataFrame(data=[["C", "B"]], columns=["A", "B"])

tm.assert_frame_equal(result, expected)
