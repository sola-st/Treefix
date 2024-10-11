# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Converts categorical columns to Categorical type.
        """
value_labels = list(value_label_dict.keys())
cat_converted_data = []
for col, label in zip(data, lbllist):
    if label in value_labels:
        # Explicit call with ordered=True
        vl = value_label_dict[label]
        keys = np.array(list(vl.keys()))
        column = data[col]
        key_matches = column.isin(keys)
        if self._using_iterator and key_matches.all():
            initial_categories: np.ndarray | None = keys
            # If all categories are in the keys and we are iterating,
            # use the same keys for all chunks. If some are missing
            # value labels, then we will fall back to the categories
            # varying across chunks.
        else:
            if self._using_iterator:
                # warn is using an iterator
                warnings.warn(
                    categorical_conversion_warning,
                    CategoricalConversionWarning,
                    stacklevel=find_stack_level(),
                )
            initial_categories = None
        cat_data = Categorical(
            column, categories=initial_categories, ordered=order_categoricals
        )
        if initial_categories is None:
            # If None here, then we need to match the cats in the Categorical
            categories = []
            for category in cat_data.categories:
                if category in vl:
                    categories.append(vl[category])
                else:
                    categories.append(category)
        else:
            # If all cats are matched, we can use the values
            categories = list(vl.values())
        try:
            # Try to catch duplicate categories
            # TODO: if we get a non-copying rename_categories, use that
            cat_data = cat_data.rename_categories(categories)
        except ValueError as err:
            vc = Series(categories).value_counts()
            repeated_cats = list(vc.index[vc > 1])
            repeats = "-" * 80 + "\n" + "\n".join(repeated_cats)
            # GH 25772
            msg = f"""
Value labels for column {col} are not unique. These cannot be converted to
pandas categoricals.

Either read the file with `convert_categoricals` set to False or use the
low level interface in `StataReader` to separately read the values and the
value_labels.

The repeated labels are:
{repeats}
"""
            raise ValueError(msg) from err
        # TODO: is the next line needed above in the data(...) method?
        cat_series = Series(cat_data, index=data.index)
        cat_converted_data.append((col, cat_series))
    else:
        cat_converted_data.append((col, data[col]))
data = DataFrame(dict(cat_converted_data), copy=False)
exit(data)
