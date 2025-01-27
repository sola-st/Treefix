# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
df = styler.data
styler1 = styler
styler2 = Styler(df.agg(["mean"]), precision=3)
styler3 = Styler(df.agg(["mean"]), precision=4)
styler1.concat(styler2.concat(styler3)).set_uuid("X")
result = styler.to_html()
# notice that the second concat (last <tr> of the output html),
# there are two `foot_` in the id and class
fp1 = "foot0_"
fp2 = "foot0_foot0_"
expected = dedent(
    f"""\
    <tr>
      <th id="T_X_level0_row1" class="row_heading level0 row1" >b</th>
      <td id="T_X_row1_col0" class="data row1 col0" >2.690000</td>
    </tr>
    <tr>
      <th id="T_X_level0_{fp1}row0" class="{fp1}row_heading level0 {fp1}row0" >mean</th>
      <td id="T_X_{fp1}row0_col0" class="{fp1}data {fp1}row0 col0" >2.650</td>
    </tr>
    <tr>
      <th id="T_X_level0_{fp2}row0" class="{fp2}row_heading level0 {fp2}row0" >mean</th>
      <td id="T_X_{fp2}row0_col0" class="{fp2}data {fp2}row0 col0" >2.6500</td>
    </tr>
  </tbody>
</table>
    """
)
assert expected in result
