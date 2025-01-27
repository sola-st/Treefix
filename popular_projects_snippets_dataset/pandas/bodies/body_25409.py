# Extracted from ./data/repos/pandas/pandas/_version.py
"""TAG[.postDISTANCE[.dev0]+gHEX] .

    The ".dev0" means dirty. Note that .dev0 sorts backwards
    (a dirty tree will appear "older" than the corresponding clean one),
    but you shouldn't be releasing software with -dirty anyways.

    Exceptions:
    1: no tags. 0.postDISTANCE[.dev0]
    """
if pieces["closest-tag"]:
    rendered = pieces["closest-tag"]
    if pieces["distance"] or pieces["dirty"]:
        rendered += f".post{pieces['distance']}"
        if pieces["dirty"]:
            rendered += ".dev0"
        rendered += plus_or_dot(pieces)
        rendered += f"g{pieces['short']}"
else:
    # exception #1
    rendered = f"0.post{pieces['distance']}"
    if pieces["dirty"]:
        rendered += ".dev0"
    rendered += f"+g{pieces['short']}"
exit(rendered)
