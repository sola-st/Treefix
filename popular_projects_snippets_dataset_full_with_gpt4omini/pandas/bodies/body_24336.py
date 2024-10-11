# Extracted from ./data/repos/pandas/pandas/io/xml.py
"""
        Parse xml nodes.

        This method will parse the children and attributes of elements
        in xpath, conditionally for only elements, only attributes
        or both while optionally renaming node names.

        Raises
        ------
        ValueError
            * If only elements and only attributes are specified.

        Notes
        -----
        Namespace URIs will be removed from return node values. Also,
        elements with missing children or attributes compared to siblings
        will have optional keys filled with None values.
        """

dicts: list[dict[str, str | None]]

if self.elems_only and self.attrs_only:
    raise ValueError("Either element or attributes can be parsed not both.")
if self.elems_only:
    if self.names:
        dicts = [
            {
                **(
                    {el.tag: el.text.strip()}
                    if el.text and not el.text.isspace()
                    else {}
                ),
                **{
                    nm: ch.text.strip() if ch.text else None
                    for nm, ch in zip(self.names, el.findall("*"))
                },
            }
            for el in elems
        ]
    else:
        dicts = [
            {
                ch.tag: ch.text.strip() if ch.text else None
                for ch in el.findall("*")
            }
            for el in elems
        ]

elif self.attrs_only:
    dicts = [
        {k: v.strip() if v else None for k, v in el.attrib.items()}
        for el in elems
    ]

else:
    if self.names:
        dicts = [
            {
                **el.attrib,
                **(
                    {el.tag: el.text.strip()}
                    if el.text and not el.text.isspace()
                    else {}
                ),
                **{
                    nm: ch.text.strip() if ch.text else None
                    for nm, ch in zip(self.names, el.findall("*"))
                },
            }
            for el in elems
        ]

    else:
        dicts = [
            {
                **el.attrib,
                **(
                    {el.tag: el.text.strip()}
                    if el.text and not el.text.isspace()
                    else {}
                ),
                **{
                    ch.tag: ch.text.strip() if ch.text else None
                    for ch in el.findall("*")
                },
            }
            for el in elems
        ]

dicts = [
    {k.split("}")[1] if "}" in k else k: v for k, v in d.items()} for d in dicts
]

keys = list(dict.fromkeys([k for d in dicts for k in d.keys()]))
dicts = [{k: d[k] if k in d.keys() else None for k in keys} for d in dicts]

if self.names:
    dicts = [dict(zip(self.names, d.values())) for d in dicts]

exit(dicts)
