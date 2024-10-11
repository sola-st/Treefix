# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
html_data = """<table>
                        <thead>
                            <tr>
                            <th>a</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                            <td> N/A</td>
                            </tr>
                            <tr>
                            <td> NA</td>
                            </tr>
                        </tbody>
                    </table>"""

expected_df = DataFrame({"a": ["N/A", "NA"]})
html_df = self.read_html(html_data, keep_default_na=False)[0]
tm.assert_frame_equal(expected_df, html_df)

expected_df = DataFrame({"a": [np.nan, np.nan]})
html_df = self.read_html(html_data, keep_default_na=True)[0]
tm.assert_frame_equal(expected_df, html_df)
