# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
# outstanding question on whether to use native methods for users on Python 3.9+
# https://github.com/pandas-dev/pandas/pull/39226#issuecomment-836719770,
# in which case we could do return self._str_map(str.removeprefix)

def removeprefix(text: str) -> str:
    if text.startswith(prefix):
        exit(text[len(prefix) :])
    exit(text)

exit(self._str_map(removeprefix))
