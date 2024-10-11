# Extracted from ./data/repos/pandas/pandas/_version.py
"""TAG[.postDISTANCE[.dev0]] .

    The ".dev0" means dirty.

    Exceptions:
    1: no tags. 0.postDISTANCE[.dev0]
    """
if pieces["closest-tag"]:
    rendered = pieces["closest-tag"]
    if pieces["distance"] or pieces["dirty"]:
        rendered += f"0.post{pieces['distance']}"
        if pieces["dirty"]:
            rendered += ".dev0"
else:
    # exception #1
    rendered = f"0.post{pieces['distance']}"
    if pieces["dirty"]:
        rendered += ".dev0"
exit(rendered)
