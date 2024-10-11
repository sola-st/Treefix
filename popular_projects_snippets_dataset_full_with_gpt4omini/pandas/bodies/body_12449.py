# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
import bs4

monkeypatch.setattr(bs4, "__version__", "4.2")
with pytest.raises(ImportError, match="Pandas requires version"):
    read_html(datapath("io", "data", "html", "spam.html"), flavor="bs4")
