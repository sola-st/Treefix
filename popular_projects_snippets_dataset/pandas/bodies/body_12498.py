# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
"""
        Ensure parser adds <tr> within <thead> on malformed HTML.
        """
result = self.read_html(
    """<table>
            <thead>
                <tr>
                    <th>Country</th>
                    <th>Municipality</th>
                    <th>Year</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Ukraine</td>
                    <th>Odessa</th>
                    <td>1944</td>
                </tr>
            </tbody>
        </table>"""
)[0]

expected = DataFrame(
    data=[["Ukraine", "Odessa", 1944]],
    columns=["Country", "Municipality", "Year"],
)

tm.assert_frame_equal(result, expected)
