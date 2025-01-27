# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
other = styler.data.agg(["mean"]).style
styler.concat(other).set_uuid("X")
result = styler.to_html()
fp = "foot0_"
expected = dedent(
    f"""\
    <tr>
      <th id="T_X_level0_row1" class="row_heading level0 row1" >b</th>
      <td id="T_X_row1_col0" class="data row1 col0" >2.690000</td>
    </tr>
    <tr>
      <th id="T_X_level0_{fp}row0" class="{fp}row_heading level0 {fp}row0" >mean</th>
      <td id="T_X_{fp}row0_col0" class="{fp}data {fp}row0 col0" >2.650000</td>
    </tr>
  </tbody>
</table>
    """
)
assert expected in result
