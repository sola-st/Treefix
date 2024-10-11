# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
pymysql = pytest.importorskip("pymysql")
cls.driver = "pymysql"
cls.connect_args = {"client_flag": pymysql.constants.CLIENT.MULTI_STATEMENTS}
