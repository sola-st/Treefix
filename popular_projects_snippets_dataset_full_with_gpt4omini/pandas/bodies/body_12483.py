# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
url = banklist_data
with pytest.raises(ValueError, match="No tables found"):
    self.read_html(
        url, match="First Federal Bank of Florida", attrs={"id": "tasdfable"}
    )
