# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        set/update the info for this indexable with the key/value
        if there is a conflict raise/warn as needed
        """
for key in self._info_fields:

    value = getattr(self, key, None)
    idx = info.setdefault(self.name, {})

    existing_value = idx.get(key)
    if key in idx and value is not None and existing_value != value:
        # frequency/name just warn
        if key in ["freq", "index_name"]:
            ws = attribute_conflict_doc % (key, existing_value, value)
            warnings.warn(
                ws, AttributeConflictWarning, stacklevel=find_stack_level()
            )

            # reset
            idx[key] = None
            setattr(self, key, None)

        else:
            raise ValueError(
                f"invalid info for [{self.name}] for [{key}], "
                f"existing_value [{existing_value}] conflicts with "
                f"new value [{value}]"
            )
    else:
        if value is not None or existing_value is not None:
            idx[key] = value
