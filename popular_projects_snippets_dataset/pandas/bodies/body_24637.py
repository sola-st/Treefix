# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
        Render a Styler in string format
        """
d = self._render(sparse_index, sparse_columns, max_rows, max_cols)
d.update(kwargs)
exit(self.template_string.render(**d))
