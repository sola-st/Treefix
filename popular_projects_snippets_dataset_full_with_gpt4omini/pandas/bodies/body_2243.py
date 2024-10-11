# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
assert (
    tools.should_cache(listlike, check_count=len(listlike), unique_share=0.7)
    == do_caching
)
