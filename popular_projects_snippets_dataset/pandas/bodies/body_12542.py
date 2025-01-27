# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# GH 29528: pd.read_html() convert <br> to space
result = self.read_html(
    """
            <table>
                <tr>
                    <th>A</th>
                </tr>
                <tr>
                    <td>word1<br>word2</td>
                </tr>
            </table>
        """
)[0]

expected = DataFrame(data=[["word1 word2"]], columns=["A"])

tm.assert_frame_equal(result, expected)
