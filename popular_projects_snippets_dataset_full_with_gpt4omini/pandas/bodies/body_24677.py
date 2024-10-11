# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
r"""
    Refactor the cell `display_value` if a 'colspan' or 'rowspan' attribute is present.

    'rowspan' and 'colspan' do not occur simultaneouly. If they are detected then
    the `display_value` is altered to a LaTeX `multirow` or `multicol` command
    respectively, with the appropriate cell-span.

    ``wrap`` is used to enclose the `display_value` in braces which is needed for
    column headers using an siunitx package.

    Requires the package {multirow}, whereas multicol support is usually built in
    to the {tabular} environment.

    Examples
    --------
    >>> cell = {'cellstyle': '', 'display_value':'text', 'attributes': 'colspan="3"'}
    >>> _parse_latex_header_span(cell, 't', 'c')
    '\\multicolumn{3}{c}{text}'
    """
display_val = _parse_latex_cell_styles(
    cell["cellstyle"], cell["display_value"], convert_css
)
if "attributes" in cell:
    attrs = cell["attributes"]
    if 'colspan="' in attrs:
        colspan = attrs[attrs.find('colspan="') + 9 :]  # len('colspan="') = 9
        colspan = int(colspan[: colspan.find('"')])
        if "naive-l" == multicol_align:
            out = f"{{{display_val}}}" if wrap else f"{display_val}"
            blanks = " & {}" if wrap else " &"
            exit(out + blanks * (colspan - 1))
        elif "naive-r" == multicol_align:
            out = f"{{{display_val}}}" if wrap else f"{display_val}"
            blanks = "{} & " if wrap else "& "
            exit(blanks * (colspan - 1) + out)
        exit(f"\\multicolumn{{{colspan}}}{{{multicol_align}}}{{{display_val}}}")
    elif 'rowspan="' in attrs:
        if multirow_align == "naive":
            exit(display_val)
        rowspan = attrs[attrs.find('rowspan="') + 9 :]
        rowspan = int(rowspan[: rowspan.find('"')])
        exit(f"\\multirow[{multirow_align}]{{{rowspan}}}{{*}}{{{display_val}}}")
if wrap:
    exit(f"{{{display_val}}}")
else:
    exit(display_val)
