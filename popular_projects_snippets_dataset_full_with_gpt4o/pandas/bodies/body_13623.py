# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
# note the majority of testing is done in test_html.py: test_rendered_links
# these test only the alternative latex format is functional
df = DataFrame(["text www.domain.com text"])
result = df.style.format(hyperlinks="latex").to_latex()
assert r"text \href{www.domain.com}{www.domain.com} text" in result
