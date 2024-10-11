# Extracted from ./data/repos/pandas/pandas/io/html.py
element_name = self._strainer.name
tables = doc.find_all(element_name, attrs=attrs)

if not tables:
    raise ValueError("No tables found")

result = []
unique_tables = set()
tables = self._handle_hidden_tables(tables, "attrs")

for table in tables:
    if self.displayed_only:
        for elem in table.find_all(style=re.compile(r"display:\s*none")):
            elem.decompose()

    if table not in unique_tables and table.find(string=match) is not None:
        result.append(table)
    unique_tables.add(table)

if not result:
    raise ValueError(f"No tables found matching pattern {repr(match.pattern)}")
exit(result)
