# Extracted from ./data/repos/pandas/pandas/_testing/_warnings.py
"""Assert that there was the expected warning among the caught warnings."""
saw_warning = False
matched_message = False
unmatched_messages = []

for actual_warning in caught_warnings:
    if issubclass(actual_warning.category, expected_warning):
        saw_warning = True

        if check_stacklevel:
            _assert_raised_with_correct_stacklevel(actual_warning)

        if match is not None:
            if re.search(match, str(actual_warning.message)):
                matched_message = True
            else:
                unmatched_messages.append(actual_warning.message)

if not saw_warning:
    raise AssertionError(
        f"Did not see expected warning of class "
        f"{repr(expected_warning.__name__)}"
    )

if match and not matched_message:
    raise AssertionError(
        f"Did not see warning {repr(expected_warning.__name__)} "
        f"matching '{match}'. The emitted warning messages are "
        f"{unmatched_messages}"
    )
