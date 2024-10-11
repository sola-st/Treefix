# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
styler = mi_styler_comp if comprehensive else mi_styler
styler.uuid_len = 5

s2 = copy.deepcopy(styler) if deepcopy else copy.copy(styler)  # make copy and check
assert s2 is not styler

if render:
    styler.to_html()

excl = [
    "cellstyle_map",  # render time vars..
    "cellstyle_map_columns",
    "cellstyle_map_index",
    "template_latex",  # render templates are class level
    "template_html",
    "template_html_style",
    "template_html_table",
]
if not deepcopy:  # check memory locations are equal for all included attributes
    for attr in [a for a in styler.__dict__ if (not callable(a) and a not in excl)]:
        assert id(getattr(s2, attr)) == id(getattr(styler, attr))
else:  # check memory locations are different for nested or mutable vars
    shallow = [
        "data",
        "columns",
        "index",
        "uuid_len",
        "uuid",
        "caption",
        "cell_ids",
        "hide_index_",
        "hide_columns_",
        "hide_index_names",
        "hide_column_names",
        "table_attributes",
    ]
    for attr in shallow:
        assert id(getattr(s2, attr)) == id(getattr(styler, attr))

    for attr in [
        a
        for a in styler.__dict__
        if (not callable(a) and a not in excl and a not in shallow)
    ]:
        if getattr(s2, attr) is None:
            assert id(getattr(s2, attr)) == id(getattr(styler, attr))
        else:
            assert id(getattr(s2, attr)) != id(getattr(styler, attr))
