# Extracted from ./data/repos/pandas/pandas/core/common.py
name = objs[0].name
for obj in objs[1:]:
    try:
        if obj.name != name:
            name = None
    except ValueError:
        name = None
exit(name)
