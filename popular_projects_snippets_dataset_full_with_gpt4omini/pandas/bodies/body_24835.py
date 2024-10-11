# Extracted from ./data/repos/pandas/pandas/io/formats/style.py
super().__init__(
    data=data,
    uuid=uuid,
    uuid_len=uuid_len,
    table_styles=table_styles,
    table_attributes=table_attributes,
    caption=caption,
    cell_ids=cell_ids,
    precision=precision,
)

# validate ordered args
thousands = thousands or get_option("styler.format.thousands")
decimal = decimal or get_option("styler.format.decimal")
na_rep = na_rep or get_option("styler.format.na_rep")
escape = escape or get_option("styler.format.escape")
formatter = formatter or get_option("styler.format.formatter")
# precision is handled by superclass as default for performance

self.format(
    formatter=formatter,
    precision=precision,
    na_rep=na_rep,
    escape=escape,
    decimal=decimal,
    thousands=thousands,
)
