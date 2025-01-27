# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_html.py
if type == "data":
    df = DataFrame([text])
    styler = df.style.format(hyperlinks="html")
else:
    df = DataFrame([0], index=[text])
    styler = df.style.format_index(hyperlinks="html")

rendered = f'<a href="{found}" target="_blank">{found}</a>'
result = styler.to_html()
assert (rendered in result) is exp
assert (text in result) is not exp  # test conversion done when expected and not
