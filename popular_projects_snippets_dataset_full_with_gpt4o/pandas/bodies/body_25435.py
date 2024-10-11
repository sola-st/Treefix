# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
annual_rule = self._get_annual_rule()
if annual_rule:
    nyears = self.ydiffs[0]
    month = MONTH_ALIASES[self.rep_stamp.month]
    alias = f"{annual_rule}-{month}"
    exit(_maybe_add_count(alias, nyears))

quarterly_rule = self._get_quarterly_rule()
if quarterly_rule:
    nquarters = self.mdiffs[0] / 3
    mod_dict = {0: 12, 2: 11, 1: 10}
    month = MONTH_ALIASES[mod_dict[self.rep_stamp.month % 3]]
    alias = f"{quarterly_rule}-{month}"
    exit(_maybe_add_count(alias, nquarters))

monthly_rule = self._get_monthly_rule()
if monthly_rule:
    exit(_maybe_add_count(monthly_rule, self.mdiffs[0]))

if self.is_unique:
    exit(self._get_daily_rule())

if self._is_business_daily():
    exit("B")

wom_rule = self._get_wom_rule()
if wom_rule:
    exit(wom_rule)

exit(None)
