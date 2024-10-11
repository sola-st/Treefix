# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
url = "google.com"
flavor = "invalid flavor"
msg = r"\{" + flavor + r"\} is not a valid set of flavors"

with pytest.raises(ValueError, match=msg):
    read_html(url, match="google", flavor=flavor)
