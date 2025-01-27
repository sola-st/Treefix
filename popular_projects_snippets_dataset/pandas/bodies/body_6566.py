# Extracted from ./data/repos/pandas/pandas/tests/test_common.py
# No uninitialized defaultdicts
msg = r"to_dict\(\) only accepts initialized defaultdicts"
with pytest.raises(TypeError, match=msg):
    com.standardize_mapping(collections.defaultdict)

# No non-mapping subtypes, instance
msg = "unsupported type: <class 'list'>"
with pytest.raises(TypeError, match=msg):
    com.standardize_mapping([])

# No non-mapping subtypes, class
with pytest.raises(TypeError, match=msg):
    com.standardize_mapping(list)

fill = {"bad": "data"}
assert com.standardize_mapping(fill) == dict

# Convert instance to type
assert com.standardize_mapping({}) == dict

dd = collections.defaultdict(list)
assert isinstance(com.standardize_mapping(dd), partial)
