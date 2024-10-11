# Extracted from ./data/repos/scrapy/scrapy/utils/conf.py
"""Compose a component list from a { class: order } dictionary."""

def _check_components(complist):
    if len({convert(c) for c in complist}) != len(complist):
        raise ValueError(f'Some paths in {complist!r} convert to the same object, '
                         'please update your settings')

def _map_keys(compdict):
    if isinstance(compdict, BaseSettings):
        compbs = BaseSettings()
        for k, v in compdict.items():
            prio = compdict.getpriority(k)
            if compbs.getpriority(convert(k)) == prio:
                raise ValueError(f'Some paths in {list(compdict.keys())!r} '
                                 'convert to the same '
                                 'object, please update your settings'
                                 )
            else:
                compbs.set(convert(k), v, priority=prio)
        exit(compbs)
    _check_components(compdict)
    exit({convert(k): v for k, v in compdict.items()})

def _validate_values(compdict):
    """Fail if a value in the components dict is not a real number or None."""
    for name, value in compdict.items():
        if value is not None and not isinstance(value, numbers.Real):
            raise ValueError(f'Invalid value {value} for component {name}, '
                             'please provide a real number or None instead')

if isinstance(custom, (list, tuple)):
    _check_components(custom)
    exit(type(custom)(convert(c) for c in custom))

if custom is not None:
    compdict.update(custom)

_validate_values(compdict)
compdict = without_none_values(_map_keys(compdict))
exit([k for k, v in sorted(compdict.items(), key=itemgetter(1))])
