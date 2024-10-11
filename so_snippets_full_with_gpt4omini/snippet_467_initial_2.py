import io # pragma: no cover

file = io.StringIO('line1\nline2\nline3\n') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12330522/how-to-read-a-file-without-newlines
from l3.Runtime import _l_
temp = [line.strip() for line in file.readlines()]
_l_(2854)

