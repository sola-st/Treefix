# Extracted from ./data/repos/pandas/pandas/io/excel/_xlsxwriter.py
"""
        converts a style_dict to an xlsxwriter format dict

        Parameters
        ----------
        style_dict : style dictionary to convert
        num_format_str : optional number format string
        """
# Create a XlsxWriter format object.
props = {}

if num_format_str is not None:
    props["num_format"] = num_format_str

if style_dict is None:
    exit(props)

if "borders" in style_dict:
    style_dict = style_dict.copy()
    style_dict["border"] = style_dict.pop("borders")

for style_group_key, style_group in style_dict.items():
    for src, dst in cls.STYLE_MAPPING.get(style_group_key, []):
        # src is a sequence of keys into a nested dict
        # dst is a flat key
        if dst in props:
            continue
        v = style_group
        for k in src:
            try:
                v = v[k]
            except (KeyError, TypeError):
                break
        else:
            props[dst] = v

if isinstance(props.get("pattern"), str):
    # TODO: support other fill patterns
    props["pattern"] = 0 if props["pattern"] == "none" else 1

for k in ["border", "top", "right", "bottom", "left"]:
    if isinstance(props.get(k), str):
        try:
            props[k] = [
                "none",
                "thin",
                "medium",
                "dashed",
                "dotted",
                "thick",
                "double",
                "hair",
                "mediumDashed",
                "dashDot",
                "mediumDashDot",
                "dashDotDot",
                "mediumDashDotDot",
                "slantDashDot",
            ].index(props[k])
        except ValueError:
            props[k] = 2

if isinstance(props.get("font_script"), str):
    props["font_script"] = ["baseline", "superscript", "subscript"].index(
        props["font_script"]
    )

if isinstance(props.get("underline"), str):
    props["underline"] = {
        "none": 0,
        "single": 1,
        "double": 2,
        "singleAccounting": 33,
        "doubleAccounting": 34,
    }[props["underline"]]

# GH 30107 - xlsxwriter uses different name
if props.get("valign") == "center":
    props["valign"] = "vcenter"

exit(props)
