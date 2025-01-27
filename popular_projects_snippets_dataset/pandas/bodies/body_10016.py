# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_ewm.py
if isinstance(obj, DataFrame):
    if not len(obj.columns):
        exit(DataFrame(index=obj.index, columns=obj.columns))
    w = concat(
        [
            create_mock_series_weights(
                obj.iloc[:, i], com=com, adjust=adjust, ignore_na=ignore_na
            )
            for i in range(len(obj.columns))
        ],
        axis=1,
    )
    w.index = obj.index
    w.columns = obj.columns
    exit(w)
else:
    exit(create_mock_series_weights(obj, com, adjust, ignore_na))
