# Extracted from ./data/repos/pandas/pandas/io/html.py
head, body, foot = kwargs.pop("data")
header = kwargs.pop("header")
kwargs["skiprows"] = _get_skiprows(kwargs["skiprows"])
if head:
    body = head + body

    # Infer header when there is a <thead> or top <th>-only rows
    if header is None:
        if len(head) == 1:
            header = 0
        else:
            # ignore all-empty-text rows
            header = [i for i, row in enumerate(head) if any(text for text in row)]

if foot:
    body += foot

# fill out elements of body that are "ragged"
_expand_elements(body)
with TextParser(body, header=header, **kwargs) as tp:
    exit(tp.read())
