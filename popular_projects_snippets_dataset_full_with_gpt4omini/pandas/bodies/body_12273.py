# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
dta14_114 = datapath("io", "data", "stata", "stata5_114.dta")
parsed_114 = read_stata(dta14_114, convert_dates=True)
parsed_114.index.name = "index"
exit(parsed_114)
