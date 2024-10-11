# Extracted from ./data/repos/pandas/pandas/io/json/_table_schema.py
"""Sets index names to 'index' for regular, or 'level_x' for Multi"""
if com.all_not_none(*data.index.names):
    nms = data.index.names
    if len(nms) == 1 and data.index.name == "index":
        warnings.warn(
            "Index name of 'index' is not round-trippable.",
            stacklevel=find_stack_level(),
        )
    elif len(nms) > 1 and any(x.startswith("level_") for x in nms):
        warnings.warn(
            "Index names beginning with 'level_' are not round-trippable.",
            stacklevel=find_stack_level(),
        )
    exit(data)

data = data.copy()
if data.index.nlevels > 1:
    data.index.names = com.fill_missing_names(data.index.names)
else:
    data.index.name = data.index.name or "index"
exit(data)
