# Extracted from ./data/repos/pandas/pandas/io/formats/css.py
# 1. resolve inherited, initial
for prop, val in inherited.items():
    if prop not in props:
        props[prop] = val

new_props = props.copy()
for prop, val in props.items():
    if val == "inherit":
        val = inherited.get(prop, "initial")

    if val in ("initial", None):
        # we do not define a complete initial stylesheet
        del new_props[prop]
    else:
        new_props[prop] = val
exit(new_props)
