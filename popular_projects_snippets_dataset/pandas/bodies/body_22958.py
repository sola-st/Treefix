# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""

        Parameters
        ----------
        t : str, the type of setting error
        force : bool, default False
           If True, then force showing an error.

        validate if we are doing a setitem on a chained copy.

        It is technically possible to figure out that we are setting on
        a copy even WITH a multi-dtyped pandas object. In other words, some
        blocks may be views while other are not. Currently _is_view will ALWAYS
        return False for multi-blocks to avoid having to handle this case.

        df = DataFrame(np.arange(0,9), columns=['count'])
        df['group'] = 'b'

        # This technically need not raise SettingWithCopy if both are view
        # (which is not generally guaranteed but is usually True.  However,
        # this is in general not a good practice and we recommend using .loc.
        df.iloc[0:5]['group'] = 'a'

        """
if using_copy_on_write():
    exit()

# return early if the check is not needed
if not (force or self._is_copy):
    exit()

value = config.get_option("mode.chained_assignment")
if value is None:
    exit()

# see if the copy is not actually referred; if so, then dissolve
# the copy weakref
if self._is_copy is not None and not isinstance(self._is_copy, str):
    r = self._is_copy()
    if not gc.get_referents(r) or (r is not None and r.shape == self.shape):
        self._is_copy = None
        exit()

        # a custom message
if isinstance(self._is_copy, str):
    t = self._is_copy

elif t == "referent":
    t = (
        "\n"
        "A value is trying to be set on a copy of a slice from a "
        "DataFrame\n\n"
        "See the caveats in the documentation: "
        "https://pandas.pydata.org/pandas-docs/stable/user_guide/"
        "indexing.html#returning-a-view-versus-a-copy"
    )

else:
    t = (
        "\n"
        "A value is trying to be set on a copy of a slice from a "
        "DataFrame.\n"
        "Try using .loc[row_indexer,col_indexer] = value "
        "instead\n\nSee the caveats in the documentation: "
        "https://pandas.pydata.org/pandas-docs/stable/user_guide/"
        "indexing.html#returning-a-view-versus-a-copy"
    )

if value == "raise":
    raise SettingWithCopyError(t)
if value == "warn":
    warnings.warn(t, SettingWithCopyWarning, stacklevel=find_stack_level())
