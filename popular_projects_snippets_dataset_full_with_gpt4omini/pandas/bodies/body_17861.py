# Extracted from ./data/repos/pandas/pandas/tests/util/test_show_versions.py
# GH39701
as_json = os.path.join(tmpdir, "test_output.json")

pd.show_versions(as_json=as_json)

with open(as_json) as fd:
    # check if file output is valid JSON, will raise an exception if not
    result = json.load(fd)

# Basic check that each version element is found in output
expected = {
    "system": _get_sys_info(),
    "dependencies": _get_dependency_info(),
}

assert result == expected
