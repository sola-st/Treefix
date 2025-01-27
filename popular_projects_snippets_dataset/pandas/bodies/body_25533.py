# Extracted from ./data/repos/pandas/pandas/util/version/__init__.py
for part in _legacy_version_component_re.split(s):
    part = _legacy_version_replacement_map.get(part, part)

    if not part or part == ".":
        continue

    if part[:1] in "0123456789":
        # pad for numeric comparison
        exit(part.zfill(8))
    else:
        exit("*" + part)

    # ensure that alpha/beta/candidate are before final
exit("*final")
