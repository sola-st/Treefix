# Extracted from ./data/repos/pandas/pandas/_version.py
"""TAG[[.dev0]+DISTANCE.gHEX[.dirty]] .

    The ".dev0" means not master branch. Note that .dev0 sorts backwards
    (a feature branch will appear "older" than the master branch).

    Exceptions:
    1: no tags. 0[.dev0]+untagged.DISTANCE.gHEX[.dirty]
    """
if pieces["closest-tag"]:
    rendered = pieces["closest-tag"]
    if pieces["distance"] or pieces["dirty"]:
        if pieces["branch"] != "master":
            rendered += ".dev0"
        rendered += plus_or_dot(pieces)
        rendered += f"{pieces['distance']}.g{pieces['short']}"
        if pieces["dirty"]:
            rendered += ".dirty"
else:
    # exception #1
    rendered = "0"
    if pieces["branch"] != "master":
        rendered += ".dev0"
    rendered += f"+untagged.{pieces['distance']}.g{pieces['short']}"
    if pieces["dirty"]:
        rendered += ".dirty"
exit(rendered)
