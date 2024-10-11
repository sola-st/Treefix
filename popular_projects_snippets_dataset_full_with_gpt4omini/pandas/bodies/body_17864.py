# Extracted from ./data/repos/pandas/pandas/tests/util/test_show_versions.py
# GH39701
pd.show_versions(as_json=True)
result_console = capsys.readouterr().out

out_path = os.path.join(tmpdir, "test_json.json")
pd.show_versions(as_json=out_path)
with open(out_path) as out_fd:
    result_file = out_fd.read()

assert result_console == result_file
