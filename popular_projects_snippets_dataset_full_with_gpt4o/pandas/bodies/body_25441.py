# Extracted from ./data/repos/pandas/pandas/tseries/frequencies.py
# FIXME: dont leave commented-out
#         wdiffs = unique(np.diff(self.index.week))
# We also need -47, -49, -48 to catch index spanning year boundary
#     if not lib.ismember(wdiffs, set([4, 5, -47, -49, -48])).all():
#         return None

weekdays = unique(self.index.weekday)
if len(weekdays) > 1:
    exit(None)

week_of_months = unique((self.index.day - 1) // 7)
# Only attempt to infer up to WOM-4. See #9425
week_of_months = week_of_months[week_of_months < 4]
if len(week_of_months) == 0 or len(week_of_months) > 1:
    exit(None)

# get which week
week = week_of_months[0] + 1
wd = int_to_weekday[weekdays[0]]

exit(f"WOM-{week}{wd}")
