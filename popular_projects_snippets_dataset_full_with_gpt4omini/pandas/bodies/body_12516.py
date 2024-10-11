# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# GH 12907
result = self.read_html(
    """<html>
            <body>
             <table>
                <thead>
                    <tr>
                        <th>Header</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1100#101</td>
                    </tr>
                </tbody>
            </table>
            </body>
        </html>""",
    decimal="#",
)[0]

expected = DataFrame(data={"Header": 1100.101}, index=[0])

assert result["Header"].dtype == np.dtype("float64")
tm.assert_frame_equal(result, expected)
