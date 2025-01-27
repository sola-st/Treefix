# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
vmin = -1000
vmax = vmin + year_span * 4
span = vmax - vmin + 1
if span < 45:  # the quarterly finder is only invoked if the span is >= 45
    exit()
nyears = span / 4
(min_anndef, maj_anndef) = converter._get_default_annual_spacing(nyears)
result = converter._quarterly_finder(vmin, vmax, "Q")
quarters = PeriodIndex(
    arrays.PeriodArray(np.array([x[0] for x in result]), freq="Q")
)
majors = np.array([x[1] for x in result])
minors = np.array([x[2] for x in result])
major_quarters = quarters[majors]
minor_quarters = quarters[minors]
check_major_years = major_quarters.year % maj_anndef == 0
check_minor_years = minor_quarters.year % min_anndef == 0
check_major_quarters = major_quarters.quarter == 1
check_minor_quarters = minor_quarters.quarter == 1
assert np.all(check_major_years)
assert np.all(check_minor_years)
assert np.all(check_major_quarters)
assert np.all(check_minor_quarters)
