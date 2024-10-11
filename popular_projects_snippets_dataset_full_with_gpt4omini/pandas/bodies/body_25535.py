# Extracted from ./data/repos/pandas/pandas/util/version/__init__.py

# Validate the version and parse it into pieces
match = self._regex.search(version)
if not match:
    raise InvalidVersion(f"Invalid version: '{version}'")

# Store the parsed out pieces of the version
self._version = _Version(
    epoch=int(match.group("epoch")) if match.group("epoch") else 0,
    release=tuple(int(i) for i in match.group("release").split(".")),
    pre=_parse_letter_version(match.group("pre_l"), match.group("pre_n")),
    post=_parse_letter_version(
        match.group("post_l"), match.group("post_n1") or match.group("post_n2")
    ),
    dev=_parse_letter_version(match.group("dev_l"), match.group("dev_n")),
    local=_parse_local_version(match.group("local")),
)

# Generate a key which will be used for sorting
self._key = _cmpkey(
    self._version.epoch,
    self._version.release,
    self._version.pre,
    self._version.post,
    self._version.dev,
    self._version.local,
)
