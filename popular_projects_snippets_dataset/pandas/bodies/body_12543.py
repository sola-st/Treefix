# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
gh_13141_data = """
          <table>
            <tr>
              <th>HTTP</th>
              <th>FTP</th>
              <th><a href="https://en.wiktionary.org/wiki/linkless">Linkless</a></th>
            </tr>
            <tr>
              <td><a href="https://en.wikipedia.org/">Wikipedia</a></td>
              <td>SURROUNDING <a href="ftp://ftp.us.debian.org/">Debian</a> TEXT</td>
              <td>Linkless</td>
            </tr>
            <tfoot>
              <tr>
                <td><a href="https://en.wikipedia.org/wiki/Page_footer">Footer</a></td>
                <td>
                  Multiple <a href="1">links:</a> <a href="2">Only first captured.</a>
                </td>
              </tr>
            </tfoot>
          </table>
          """

gh_13141_expected = {
    "head_ignore": ["HTTP", "FTP", "Linkless"],
    "head_extract": [
        ("HTTP", None),
        ("FTP", None),
        ("Linkless", "https://en.wiktionary.org/wiki/linkless"),
    ],
    "body_ignore": ["Wikipedia", "SURROUNDING Debian TEXT", "Linkless"],
    "body_extract": [
        ("Wikipedia", "https://en.wikipedia.org/"),
        ("SURROUNDING Debian TEXT", "ftp://ftp.us.debian.org/"),
        ("Linkless", None),
    ],
    "footer_ignore": [
        "Footer",
        "Multiple links: Only first captured.",
        None,
    ],
    "footer_extract": [
        ("Footer", "https://en.wikipedia.org/wiki/Page_footer"),
        ("Multiple links: Only first captured.", "1"),
        None,
    ],
}

data_exp = gh_13141_expected["body_ignore"]
foot_exp = gh_13141_expected["footer_ignore"]
head_exp = gh_13141_expected["head_ignore"]
if arg == "all":
    data_exp = gh_13141_expected["body_extract"]
    foot_exp = gh_13141_expected["footer_extract"]
    head_exp = gh_13141_expected["head_extract"]
elif arg == "body":
    data_exp = gh_13141_expected["body_extract"]
elif arg == "footer":
    foot_exp = gh_13141_expected["footer_extract"]
elif arg == "header":
    head_exp = gh_13141_expected["head_extract"]

result = self.read_html(gh_13141_data, extract_links=arg)[0]
expected = DataFrame([data_exp, foot_exp], columns=head_exp)
tm.assert_frame_equal(result, expected)
