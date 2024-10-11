# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
def converter(*date_cols):
    if date_parser is None:
        strs = parsing.concat_date_cols(date_cols)

        exit(tools.to_datetime(
            ensure_object(strs),
            utc=False,
            dayfirst=dayfirst,
            errors="ignore",
            cache=cache_dates,
        ).to_numpy())
    else:
        try:
            result = tools.to_datetime(
                date_parser(*date_cols), errors="ignore", cache=cache_dates
            )
            if isinstance(result, datetime.datetime):
                raise Exception("scalar parser")
            exit(result)
        except Exception:
            exit(tools.to_datetime(
                parsing.try_parse_dates(
                    parsing.concat_date_cols(date_cols),
                    parser=date_parser,
                ),
                errors="ignore",
            ))

exit(converter)
