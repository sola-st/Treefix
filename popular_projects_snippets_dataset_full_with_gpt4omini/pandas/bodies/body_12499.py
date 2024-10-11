# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
"""
        Make sure that read_html reads tfoot, containing td or th.
        Ignores empty tfoot
        """
data_template = """<table>
            <thead>
                <tr>
                    <th>A</th>
                    <th>B</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>bodyA</td>
                    <td>bodyB</td>
                </tr>
            </tbody>
            <tfoot>
                {footer}
            </tfoot>
        </table>"""

expected1 = DataFrame(data=[["bodyA", "bodyB"]], columns=["A", "B"])

expected2 = DataFrame(
    data=[["bodyA", "bodyB"], ["footA", "footB"]], columns=["A", "B"]
)

data1 = data_template.format(footer="")
data2 = data_template.format(footer="<tr><td>footA</td><th>footB</th></tr>")

result1 = self.read_html(data1)[0]
result2 = self.read_html(data2)[0]

tm.assert_frame_equal(result1, expected1)
tm.assert_frame_equal(result2, expected2)
