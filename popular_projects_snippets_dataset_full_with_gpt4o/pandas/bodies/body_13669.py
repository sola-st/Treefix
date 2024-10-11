# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
assert foot_prefix.endswith("_") or foot_prefix == ""
fp = foot_prefix
exit(indent(
    dedent(
        f"""\
        <tr>
          <th id="T_X_level0_{fp}row0" class="{fp}row_heading level0 {fp}row0" >a</th>
          <td id="T_X_{fp}row0_col0" class="{fp}data {fp}row0 col0" >2.610000</td>
        </tr>
        <tr>
          <th id="T_X_level0_{fp}row1" class="{fp}row_heading level0 {fp}row1" >b</th>
          <td id="T_X_{fp}row1_col0" class="{fp}data {fp}row1 col0" >2.690000</td>
        </tr>
        """
    ),
    prefix=" " * 4,
))
