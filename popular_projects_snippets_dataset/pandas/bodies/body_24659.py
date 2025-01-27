# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
    looks for multiple CSS selectors and separates them:
    [{'selector': 'td, th', 'props': 'a:v;'}]
        ---> [{'selector': 'td', 'props': 'a:v;'},
              {'selector': 'th', 'props': 'a:v;'}]
    """
exit([
    {"selector": selector, "props": css_dict["props"]}
    for css_dict in styles
    for selector in css_dict["selector"].split(",")
])
