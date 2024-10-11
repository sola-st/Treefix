# Extracted from ./data/repos/pandas/pandas/io/formats/html.py
self.fmt = formatter
self.classes = classes

self.frame = self.fmt.frame
self.columns = self.fmt.tr_frame.columns
self.elements: list[str] = []
self.bold_rows = self.fmt.bold_rows
self.escape = self.fmt.escape
self.show_dimensions = self.fmt.show_dimensions
if border is None or border is True:
    border = cast(int, get_option("display.html.border"))
elif not border:
    border = None

self.border = border
self.table_id = table_id
self.render_links = render_links

self.col_space = {
    column: f"{value}px" if isinstance(value, int) else value
    for column, value in self.fmt.col_space.items()
}
