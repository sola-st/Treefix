# Extracted from ./data/repos/scrapy/scrapy/utils/conf.py
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
