# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""validate against an existing table"""
if other is None:
    exit()

if other.table_type != self.table_type:
    raise TypeError(
        "incompatible table_type with existing "
        f"[{other.table_type} - {self.table_type}]"
    )

for c in ["index_axes", "non_index_axes", "values_axes"]:
    sv = getattr(self, c, None)
    ov = getattr(other, c, None)
    if sv != ov:

        # show the error for the specific axes
        # Argument 1 to "enumerate" has incompatible type
        # "Optional[Any]"; expected "Iterable[Any]"  [arg-type]
        for i, sax in enumerate(sv):  # type: ignore[arg-type]
            # Value of type "Optional[Any]" is not indexable  [index]
            oax = ov[i]  # type: ignore[index]
            if sax != oax:
                raise ValueError(
                    f"invalid combination of [{c}] on appending data "
                    f"[{sax}] vs current table [{oax}]"
                )

                # should never get here
        raise Exception(
            f"invalid combination of [{c}] on appending data [{sv}] vs "
            f"current table [{ov}]"
        )
