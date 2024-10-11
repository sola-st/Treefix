# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_spec_conformance.py
df = df_from_dict(
    {"weekday": ["Mon", "Tue", "Mon", "Wed", "Mon", "Thu", "Fri", "Sat", "Sun"]},
    is_categorical=True,
)

colX = df.__dataframe__().get_column_by_name("weekday")
categorical = colX.describe_categorical
assert isinstance(categorical["is_ordered"], bool)
assert isinstance(categorical["is_dictionary"], bool)
