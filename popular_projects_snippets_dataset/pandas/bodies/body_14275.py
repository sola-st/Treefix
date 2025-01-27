# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_printing.py
ipython = ip.instance(config=ip.config)
df = pd.DataFrame({"A": [1, 2]})
objects = [df["A"], df, df]  # dataframe / series
expected_keys = [
    {"text/plain", "application/vnd.dataresource+json"},
    {"text/plain", "text/html", "application/vnd.dataresource+json"},
]

opt = pd.option_context("display.html.table_schema", True)
for obj, expected in zip(objects, expected_keys):
    with opt:
        formatted = ipython.display_formatter.format(obj)
    assert set(formatted[0].keys()) == expected

with_latex = pd.option_context("styler.render.repr", "latex")

with opt, with_latex:
    formatted = ipython.display_formatter.format(obj)

expected = {
    "text/plain",
    "text/html",
    "text/latex",
    "application/vnd.dataresource+json",
}
assert set(formatted[0].keys()) == expected
