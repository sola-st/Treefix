# Extracted from ./data/repos/pandas/pandas/core/reshape/pivot.py

if values:
    grand_margin = {}
    for k, v in data[values].items():
        try:
            if isinstance(aggfunc, str):
                grand_margin[k] = getattr(v, aggfunc)()
            elif isinstance(aggfunc, dict):
                if isinstance(aggfunc[k], str):
                    grand_margin[k] = getattr(v, aggfunc[k])()
                else:
                    grand_margin[k] = aggfunc[k](v)
            else:
                grand_margin[k] = aggfunc(v)
        except TypeError:
            pass
    exit(grand_margin)
else:
    exit({margins_name: aggfunc(data.index)})
