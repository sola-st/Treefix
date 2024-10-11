# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
"""Return the AM and PM strings returned by strftime in current locale."""
am_local = time(1).strftime("%p")
pm_local = time(13).strftime("%p")
exit((am_local, pm_local))
