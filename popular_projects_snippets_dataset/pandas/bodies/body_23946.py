# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Create a pytables index on the specified columns.

        Parameters
        ----------
        columns : None, bool, or listlike[str]
            Indicate which columns to create an index on.

            * False : Do not create any indexes.
            * True : Create indexes on all columns.
            * None : Create indexes on all columns.
            * listlike : Create indexes on the given columns.

        optlevel : int or None, default None
            Optimization level, if None, pytables defaults to 6.
        kind : str or None, default None
            Kind of index, if None, pytables defaults to "medium".

        Raises
        ------
        TypeError if trying to create an index on a complex-type column.

        Notes
        -----
        Cannot index Time64Col or ComplexCol.
        Pytables must be >= 3.0.
        """
if not self.infer_axes():
    exit()
if columns is False:
    exit()

# index all indexables and data_columns
if columns is None or columns is True:
    columns = [a.cname for a in self.axes if a.is_data_indexable]
if not isinstance(columns, (tuple, list)):
    columns = [columns]

kw = {}
if optlevel is not None:
    kw["optlevel"] = optlevel
if kind is not None:
    kw["kind"] = kind

table = self.table
for c in columns:
    v = getattr(table.cols, c, None)
    if v is not None:
        # remove the index if the kind/optlevel have changed
        if v.is_indexed:
            index = v.index
            cur_optlevel = index.optlevel
            cur_kind = index.kind

            if kind is not None and cur_kind != kind:
                v.remove_index()
            else:
                kw["kind"] = cur_kind

            if optlevel is not None and cur_optlevel != optlevel:
                v.remove_index()
            else:
                kw["optlevel"] = cur_optlevel

                # create the index
        if not v.is_indexed:
            if v.type.startswith("complex"):
                raise TypeError(
                    "Columns containing complex values can be stored but "
                    "cannot be indexed when using table format. Either use "
                    "fixed format, set index=False, or do not include "
                    "the columns containing complex values to "
                    "data_columns when initializing the table."
                )
            v.create_index(**kw)
    elif c in self.non_index_axes[0][1]:
        # GH 28156
        raise AttributeError(
            f"column {c} is not a data_column.\n"
            f"In order to read column {c} you must reload the dataframe \n"
            f"into HDFStore and include {c} with the data_columns argument."
        )
