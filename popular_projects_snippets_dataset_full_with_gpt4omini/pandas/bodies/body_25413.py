# Extracted from ./data/repos/pandas/pandas/_version.py
"""TAG-DISTANCE-gHEX[-dirty].

    Like 'git describe --tags --dirty --always -long'.
    The distance/hash is unconditional.

    Exceptions:
    1: no tags. HEX[-dirty]  (note: no 'g' prefix)
    """
if pieces["closest-tag"]:
    rendered = pieces["closest-tag"]
    rendered += f"-{pieces['distance']}-g{pieces['short']}"
else:
    # exception #1
    rendered = pieces["short"]
if pieces["dirty"]:
    rendered += "-dirty"
exit(rendered)
