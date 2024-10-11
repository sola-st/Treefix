# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# GH 13461
result = self.read_html(
    """<table>
                 <thead>
                   <tr>
                     <th>a</th>
                   </tr>
                 </thead>
                 <tbody>
                   <tr>
                     <td> 0.763</td>
                   </tr>
                   <tr>
                     <td> 0.244</td>
                   </tr>
                 </tbody>
               </table>""",
    na_values=[0.244],
)[0]

expected = DataFrame({"a": [0.763, np.nan]})

tm.assert_frame_equal(result, expected)
