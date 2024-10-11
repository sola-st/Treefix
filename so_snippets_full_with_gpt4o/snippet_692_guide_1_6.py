import io # pragma: no cover
import re # pragma: no cover
import pandas as pd # pragma: no cover

df_str = ''' # pragma: no cover
| int_score | ext_score | eligible | # pragma: no cover
|           | 701       | True     | # pragma: no cover
| 221.3     | 0         | False    | # pragma: no cover
|           | 576       | True     | # pragma: no cover
| 300       | 600       | True     | # pragma: no cover
''' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/22604564/create-pandas-dataframe-from-a-string
from l3.Runtime import _l_
try:
    import io
    _l_(14181)

except ImportError:
    pass
try:
    import re
    _l_(14183)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(14185)

except ImportError:
    pass


def read_psv(str_input: str, **kwargs) -> pd.DataFrame:
    _l_(14192)

    """Read a Pandas object from a pipe-separated table contained within a string.

    Input example:
        | int_score | ext_score | eligible |
        |           | 701       | True     |
        | 221.3     | 0         | False    |
        |           | 576       | True     |
        | 300       | 600       | True     |

    The leading and trailing pipes are optional, but if one is present,
    so must be the other.

    `kwargs` are passed to `read_csv`. They must not include `sep`.

    In PyCharm, the "Pipe Table Formatter" plugin has a "Format" feature that can 
    be used to neatly format a table.

    Ref: https://stackoverflow.com/a/46471952/
    """

    substitutions = [
        ('^ *', ''),  # Remove leading spaces
        (' *$', ''),  # Remove trailing spaces
        (r' *\| *', '|'),  # Remove spaces between columns
    ]
    _l_(14186)
    if all(line.lstrip().startswith('|') and line.rstrip().endswith('|') for line in str_input.strip().split('\n')):
        _l_(14188)

        substitutions.extend([
            (r'^\|', ''),  # Remove redundant leading delimiter
            (r'\|$', ''),  # Remove redundant trailing delimiter
        ])
        _l_(14187)
    for pattern, replacement in substitutions:
        _l_(14190)

        str_input = re.sub(pattern, replacement, str_input, flags=re.MULTILINE)
        _l_(14189)
    aux = pd.read_csv(io.StringIO(str_input), sep='|', **kwargs)
    _l_(14191)
    return aux


df = pd.read_csv(io.StringIO(df_str), sep=r'\s*\|\s*', engine='python')
_l_(14193)

