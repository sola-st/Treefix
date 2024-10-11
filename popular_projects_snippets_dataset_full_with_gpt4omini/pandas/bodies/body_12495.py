# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
"""
        Make sure that read_html ignores empty tables.
        """
html = """
            <table>
                <thead>
                    <tr>
                        <th>A</th>
                        <th>B</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>2</td>
                    </tr>
                </tbody>
            </table>
            <table>
                <tbody>
                </tbody>
            </table>
        """
result = self.read_html(html)
assert len(result) == 1
