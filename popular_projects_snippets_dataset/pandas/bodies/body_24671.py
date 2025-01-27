# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
        Combine the ``_Tooltips`` CSS class name and CSS properties to the format
        required to extend the underlying ``Styler`` `table_styles` to allow
        tooltips to render in HTML.

        Returns
        -------
        styles : List
        """
exit([
    {
        "selector": f".{self.class_name}",
        "props": maybe_convert_css_to_tuples(self.class_properties),
    }
])
