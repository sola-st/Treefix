# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
if css_styles and css_converter:
    # Use dict to get only one (case-insensitive) declaration per property
    declaration_dict = {
        prop.lower(): val for prop, val in css_styles[css_row, css_col]
    }
    # Convert to frozenset for order-invariant caching
    unique_declarations = frozenset(declaration_dict.items())
    style = css_converter(unique_declarations)

super().__init__(row=row, col=col, val=val, style=style, **kwargs)
