# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# GH5048: if header is specified explicitly, an int column should be
# parsed as int while its header is parsed as str
result = self.read_html(
    """
            <table>
                <tr>
                    <td>S</td>
                    <td>I</td>
                </tr>
                <tr>
                    <td>text</td>
                    <td>1944</td>
                </tr>
            </table>
        """,
    header=0,
)[0]

expected = DataFrame([["text", 1944]], columns=("S", "I"))

tm.assert_frame_equal(result, expected)
