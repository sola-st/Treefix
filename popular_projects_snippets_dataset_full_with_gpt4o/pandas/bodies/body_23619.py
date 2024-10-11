# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Checks column names to ensure that they are valid Stata column names.
        This includes checks for:
            * Non-string names
            * Stata keywords
            * Variables that start with numbers
            * Variables with names that are too long

        When an illegal variable name is detected, it is converted, and if
        dates are exported, the variable name is propagated to the date
        conversion dictionary
        """
converted_names: dict[Hashable, str] = {}
columns = list(data.columns)
original_columns = columns[:]

duplicate_var_id = 0
for j, name in enumerate(columns):
    orig_name = name
    if not isinstance(name, str):
        name = str(name)

    name = self._validate_variable_name(name)

    # Variable name must not be a reserved word
    if name in self.RESERVED_WORDS:
        name = "_" + name

    # Variable name may not start with a number
    if "0" <= name[0] <= "9":
        name = "_" + name

    name = name[: min(len(name), 32)]

    if not name == orig_name:
        # check for duplicates
        while columns.count(name) > 0:
            # prepend ascending number to avoid duplicates
            name = "_" + str(duplicate_var_id) + name
            name = name[: min(len(name), 32)]
            duplicate_var_id += 1
        converted_names[orig_name] = name

    columns[j] = name

data.columns = Index(columns)

# Check date conversion, and fix key if needed
if self._convert_dates:
    for c, o in zip(columns, original_columns):
        if c != o:
            self._convert_dates[c] = self._convert_dates[o]
            del self._convert_dates[o]

if converted_names:
    conversion_warning = []
    for orig_name, name in converted_names.items():
        msg = f"{orig_name}   ->   {name}"
        conversion_warning.append(msg)

    ws = invalid_name_doc.format("\n    ".join(conversion_warning))
    warnings.warn(
        ws,
        InvalidColumnName,
        stacklevel=find_stack_level(),
    )

self._converted_names = converted_names
self._update_strl_names()

exit(data)
