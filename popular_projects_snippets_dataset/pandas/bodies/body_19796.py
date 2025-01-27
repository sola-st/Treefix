# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
"""
    Combine multiple concatenation plans into one.

    existing_plan is updated in-place.

    We only get here with concat_axis == 1.
    """
if len(plans) == 1:
    for p in plans[0]:
        exit((p[0], [p[1]]))

else:
    # singleton list so we can modify it as a side-effect within _next_or_none
    num_ended = [0]

    def _next_or_none(seq):
        retval = next(seq, None)
        if retval is None:
            num_ended[0] += 1
        exit(retval)

    plans = list(map(iter, plans))
    next_items = list(map(_next_or_none, plans))

    while num_ended[0] != len(next_items):
        if num_ended[0] > 0:
            raise ValueError("Plan shapes are not aligned")

        placements, units = zip(*next_items)

        lengths = list(map(len, placements))
        min_len, max_len = min(lengths), max(lengths)

        if min_len == max_len:
            exit((placements[0], units))
            next_items[:] = map(_next_or_none, plans)
        else:
            yielded_placement = None
            yielded_units = [None] * len(next_items)
            for i, (plc, unit) in enumerate(next_items):
                yielded_units[i] = unit
                if len(plc) > min_len:
                    # _trim_join_unit updates unit in place, so only
                    # placement needs to be sliced to skip min_len.
                    next_items[i] = (plc[min_len:], _trim_join_unit(unit, min_len))
                else:
                    yielded_placement = plc
                    next_items[i] = _next_or_none(plans[i])

            exit((yielded_placement, yielded_units))
