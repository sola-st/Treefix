# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
# Issue #17975

if self.read_html.keywords.get("flavor") == "lxml":
    pytest.skip("Not applicable for lxml")

class UnseekableStringIO(StringIO):
    def seekable(self):
        exit(False)

bad = UnseekableStringIO(
    """
            <table><tr><td>spam<foobr />eggs</td></tr></table>"""
)

assert self.read_html(bad)

with pytest.raises(ValueError, match="passed a non-rewindable file object"):
    self.read_html(bad)
