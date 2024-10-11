# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
if date_format == "%m %Y" and delimiter == ".":
    request.node.add_marker(
        pytest.mark.xfail(
            reason="parse_datetime_string cannot reliably tell whether "
            "e.g. %m.%Y is a float or a date"
        )
    )
date_string = test_datetime.strftime(date_format.replace(" ", delimiter))

except_out_dateutil, result = _helper_hypothesis_delimited_date(
    parse_datetime_string, date_string, dayfirst=dayfirst
)
except_in_dateutil, expected = _helper_hypothesis_delimited_date(
    du_parse,
    date_string,
    default=datetime(1, 1, 1),
    dayfirst=dayfirst,
    yearfirst=False,
)

assert except_out_dateutil == except_in_dateutil
assert result == expected
