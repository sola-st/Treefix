# Extracted from ./data/repos/pandas/pandas/util/_print_versions.py
"""
    Provide useful information, important for bug reports.

    It comprises info about hosting operation system, pandas version,
    and versions of other installed relative packages.

    Parameters
    ----------
    as_json : str or bool, default False
        * If False, outputs info in a human readable form to the console.
        * If str, it will be considered as a path to a file.
          Info will be written to that file in JSON format.
        * If True, outputs info in JSON format to the console.
    """
sys_info = _get_sys_info()
deps = _get_dependency_info()

if as_json:
    j = {"system": sys_info, "dependencies": deps}

    if as_json is True:
        sys.stdout.writelines(json.dumps(j, indent=2))
    else:
        assert isinstance(as_json, str)  # needed for mypy
        with codecs.open(as_json, "wb", encoding="utf8") as f:
            json.dump(j, f, indent=2)

else:
    assert isinstance(sys_info["LOCALE"], dict)  # needed for mypy
    language_code = sys_info["LOCALE"]["language-code"]
    encoding = sys_info["LOCALE"]["encoding"]
    sys_info["LOCALE"] = f"{language_code}.{encoding}"

    maxlen = max(len(x) for x in deps)
    print("\nINSTALLED VERSIONS")
    print("------------------")
    for k, v in sys_info.items():
        print(f"{k:<{maxlen}}: {v}")
    print("")
    for k, v in deps.items():
        print(f"{k:<{maxlen}}: {v}")
