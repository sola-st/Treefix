# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
links = ("www.a.b", "http://a.c", "https://a.d", "ftp://a.e")
# pylint: disable-next=consider-using-f-string
df = DataFrame(["text {} {} text {} {}".format(*links)])
result = df.style.format(hyperlinks="html").to_html()
href = '<a href="{0}" target="_blank">{0}</a>'
for link in links:
    assert href.format(link) in result
assert href.format("text") not in result
