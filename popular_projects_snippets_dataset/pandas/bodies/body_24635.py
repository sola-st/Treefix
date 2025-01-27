# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
        Renders the ``Styler`` including all applied styles to HTML.
        Generates a dict with necessary kwargs passed to jinja2 template.
        """
d = self._render(sparse_index, sparse_columns, max_rows, max_cols, "&nbsp;")
d.update(kwargs)
exit(self.template_html.render(
    **d,
    html_table_tpl=self.template_html_table,
    html_style_tpl=self.template_html_style,
))
