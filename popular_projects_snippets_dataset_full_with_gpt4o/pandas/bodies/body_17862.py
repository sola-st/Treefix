# Extracted from ./data/repos/pandas/pandas/tests/util/test_show_versions.py
# GH39701
pd.show_versions(as_json=True)
stdout = capsys.readouterr().out

# check valid json is printed to the console if as_json is True
result = json.loads(stdout)

# Basic check that each version element is found in output
expected = {
    "system": _get_sys_info(),
    "dependencies": _get_dependency_info(),
}

assert result == expected
