# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/index.html"  # noqa E501
df1 = self.read_html(
    # lxml cannot find attrs leave out for now
    url,
    match="First Federal Bank of Florida",  # attrs={"class": "dataTable"}
)
# lxml cannot find attrs leave out for now
df2 = self.read_html(
    url,
    match="Metcalf Bank",
)  # attrs={"class": "dataTable"})

assert_framelist_equal(df1, df2)
