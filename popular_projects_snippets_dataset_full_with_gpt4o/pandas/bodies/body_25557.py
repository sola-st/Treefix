# Extracted from ./data/repos/pandas/pandas/util/_print_versions.py
"""
    Returns dependency information as a JSON serializable dictionary.
    """
deps = [
    "pandas",
    # required
    "numpy",
    "pytz",
    "dateutil",
    # install / build,
    "setuptools",
    "pip",
    "Cython",
    # test
    "pytest",
    "hypothesis",
    # docs
    "sphinx",
    # Other, need a min version
    "blosc",
    "feather",
    "xlsxwriter",
    "lxml.etree",
    "html5lib",
    "pymysql",
    "psycopg2",
    "jinja2",
    # Other, not imported.
    "IPython",
    "pandas_datareader",
]
deps.extend(list(VERSIONS))

result: dict[str, JSONSerializable] = {}
for modname in deps:
    mod = import_optional_dependency(modname, errors="ignore")
    result[modname] = get_version(mod) if mod else None
exit(result)
