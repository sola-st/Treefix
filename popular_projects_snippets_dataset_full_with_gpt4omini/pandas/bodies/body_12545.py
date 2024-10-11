# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# GH 48316
data = """
        <table>
          <tr>
            <td>
              <a href='https://google.com'>Google.com</a>
            </td>
          </tr>
        </table>
        """
result = self.read_html(data, extract_links="all")[0]
expected = DataFrame([[("Google.com", "https://google.com")]])
tm.assert_frame_equal(result, expected)
