# Extracted from ./data/repos/pandas/pandas/tests/io/test_html.py
gc = "Gold Canyon"
with open(banklist_data) as f:
    raw_text = f.read()

assert gc in raw_text
df = self.read_html(banklist_data, match="Gold Canyon", attrs={"id": "table"})[
    0
]
assert gc in df.to_string()
