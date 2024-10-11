# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
"""
        Don't fail with bs4 when there is a header and only one column
        as described in issue #9178
        """
result = self.read_html(
    """<table>
                <thead>
                    <tr>
                        <th>Header</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>first</td>
                    </tr>
                </tbody>
            </table>"""
)[0]

expected = DataFrame(data={"Header": "first"}, index=[0])

tm.assert_frame_equal(result, expected)
