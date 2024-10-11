# Extracted from ./data/repos/pandas/pandas/io/xml.py
"""
        Iterparse xml nodes.

        This method will read in local disk, decompressed XML files for elements
        and underlying descendants using iterparse, a method to iterate through
        an XML tree without holding entire XML tree in memory.

        Raises
        ------
        TypeError
            * If `iterparse` is not a dict or its dict value is not list-like.
        ParserError
            * If `path_or_buffer` is not a physical file on disk or file-like object.
            * If no data is returned from selected items in `iterparse`.

        Notes
        -----
        Namespace URIs will be removed from return node values. Also,
        elements with missing children or attributes in submitted list
        will have optional keys filled with None values.
        """

dicts: list[dict[str, str | None]] = []
row: dict[str, str | None] | None = None

if not isinstance(self.iterparse, dict):
    raise TypeError(
        f"{type(self.iterparse).__name__} is not a valid type for iterparse"
    )

row_node = next(iter(self.iterparse.keys())) if self.iterparse else ""
if not is_list_like(self.iterparse[row_node]):
    raise TypeError(
        f"{type(self.iterparse[row_node])} is not a valid type "
        "for value in iterparse"
    )

if (not hasattr(self.path_or_buffer, "read")) and (
    not isinstance(self.path_or_buffer, str)
    or is_url(self.path_or_buffer)
    or is_fsspec_url(self.path_or_buffer)
    or self.path_or_buffer.startswith(("<?xml", "<"))
    or infer_compression(self.path_or_buffer, "infer") is not None
):
    raise ParserError(
        "iterparse is designed for large XML files that are fully extracted on "
        "local disk and not as compressed files or online sources."
    )

for event, elem in iterparse(self.path_or_buffer, events=("start", "end")):
    curr_elem = elem.tag.split("}")[1] if "}" in elem.tag else elem.tag

    if event == "start":
        if curr_elem == row_node:
            row = {}

    if row is not None:
        if self.names:
            for col, nm in zip(self.iterparse[row_node], self.names):
                if curr_elem == col:
                    elem_val = elem.text.strip() if elem.text else None
                    if row.get(nm) != elem_val and nm not in row:
                        row[nm] = elem_val
                if col in elem.attrib:
                    if elem.attrib[col] not in row.values() and nm not in row:
                        row[nm] = elem.attrib[col]
        else:
            for col in self.iterparse[row_node]:
                if curr_elem == col:
                    row[col] = elem.text.strip() if elem.text else None
                if col in elem.attrib:
                    row[col] = elem.attrib[col]

    if event == "end":
        if curr_elem == row_node and row is not None:
            dicts.append(row)
            row = None

        elem.clear()
        if hasattr(elem, "getprevious"):
            while (
                elem.getprevious() is not None and elem.getparent() is not None
            ):
                del elem.getparent()[0]

if dicts == []:
    raise ParserError("No result from selected items in iterparse.")

keys = list(dict.fromkeys([k for d in dicts for k in d.keys()]))
dicts = [{k: d[k] if k in d.keys() else None for k in keys} for d in dicts]

if self.names:
    dicts = [dict(zip(self.names, d.values())) for d in dicts]

exit(dicts)
