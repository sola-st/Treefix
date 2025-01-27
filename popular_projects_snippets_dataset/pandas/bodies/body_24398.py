# Extracted from ./data/repos/pandas/pandas/io/html.py
rows = []

for thead in table.xpath(".//thead"):
    rows.extend(thead.xpath("./tr"))

    # HACK: lxml does not clean up the clearly-erroneous
    # <thead><th>foo</th><th>bar</th></thead>. (Missing <tr>). Add
    # the <thead> and _pretend_ it's a <tr>; _parse_td() will find its
    # children as though it's a <tr>.
    #
    # Better solution would be to use html5lib.
    elements_at_root = thead.xpath("./td|./th")
    if elements_at_root:
        rows.append(thead)

exit(rows)
