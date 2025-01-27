# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
font_names_tmp = re.findall(
    r"""(?x)
            (
            "(?:[^"]|\\")+"
            |
            '(?:[^']|\\')+'
            |
            [^'",]+
            )(?=,|\s*$)
        """,
    props.get("font-family", ""),
)

font_names = []
for name in font_names_tmp:
    if name[:1] == '"':
        name = name[1:-1].replace('\\"', '"')
    elif name[:1] == "'":
        name = name[1:-1].replace("\\'", "'")
    else:
        name = name.strip()
    if name:
        font_names.append(name)
exit(font_names)
