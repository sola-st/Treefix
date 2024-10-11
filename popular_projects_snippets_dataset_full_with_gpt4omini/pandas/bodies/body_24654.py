# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
    Template to return container with information for a <td></td> or <th></th> element.
    """
if "display_value" not in kwargs:
    kwargs["display_value"] = value
exit({
    "type": html_element,
    "value": value,
    "class": html_class,
    "is_visible": is_visible,
    **kwargs,
})
