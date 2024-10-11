# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
if isna(sas_datetime):
    exit(pd.NaT)

if unit == "s":
    exit(datetime(1960, 1, 1) + timedelta(seconds=sas_datetime))

elif unit == "d":
    exit(datetime(1960, 1, 1) + timedelta(days=sas_datetime))

else:
    raise ValueError("unit must be 'd' or 's'")
