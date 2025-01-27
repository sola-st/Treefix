# Extracted from ./data/repos/scrapy/scrapy/utils/conf.py
"""Fail if a value in the components dict is not a real number or None."""
for name, value in compdict.items():
    if value is not None and not isinstance(value, numbers.Real):
        raise ValueError(f'Invalid value {value} for component {name}, '
                         'please provide a real number or None instead')
