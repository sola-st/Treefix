# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# GH 20027
data = StringIO(
    """<html>
          <body>
            <table>
              <tr>
                <td>
                  foo
                  <span style="display:none;text-align:center">bar</span>
                  <span style="display:none">baz</span>
                  <span style="display: none">qux</span>
                </td>
              </tr>
            </table>
            <table style="display: none">
              <tr>
                <td>foo</td>
              </tr>
            </table>
          </body>
        </html>"""
)

dfs = self.read_html(data, displayed_only=displayed_only)
tm.assert_frame_equal(dfs[0], exp0)

if exp1 is not None:
    tm.assert_frame_equal(dfs[1], exp1)
else:
    assert len(dfs) == 1  # Should not parse hidden table
