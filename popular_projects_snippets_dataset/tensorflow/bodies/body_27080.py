# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/sql_dataset_test.py
super(SqlDatasetTestBase, self).setUp()
self.data_source_name = os.path.join(test.get_temp_dir(), "tftest.sqlite")

conn = sqlite3.connect(self.data_source_name)
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS students")
c.execute("DROP TABLE IF EXISTS people")
c.execute("DROP TABLE IF EXISTS townspeople")
c.execute("DROP TABLE IF EXISTS data")
c.execute(
    "CREATE TABLE IF NOT EXISTS students (id INTEGER NOT NULL PRIMARY KEY, "
    "first_name VARCHAR(100), last_name VARCHAR(100), motto VARCHAR(100), "
    "school_id VARCHAR(100), favorite_nonsense_word VARCHAR(100), "
    "desk_number INTEGER, income INTEGER, favorite_number INTEGER, "
    "favorite_big_number INTEGER, favorite_negative_number INTEGER, "
    "favorite_medium_sized_number INTEGER, brownie_points INTEGER, "
    "account_balance INTEGER, registration_complete INTEGER)")
c.executemany(
    "INSERT INTO students (first_name, last_name, motto, school_id, "
    "favorite_nonsense_word, desk_number, income, favorite_number, "
    "favorite_big_number, favorite_negative_number, "
    "favorite_medium_sized_number, brownie_points, account_balance, "
    "registration_complete) "
    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    [("John", "Doe", "Hi!", "123", "n\0nsense", 9, 0, 2147483647,
      9223372036854775807, -2, 32767, 0, 0, 1),
     ("Jane", "Moe", "Hi again!", "1000", "nonsense\0", 127, -20000,
      -2147483648, -9223372036854775808, -128, -32768, 255, 65535, 0)])
c.execute(
    "CREATE TABLE IF NOT EXISTS people (id INTEGER NOT NULL PRIMARY KEY, "
    "first_name VARCHAR(100), last_name VARCHAR(100), state VARCHAR(100))")
c.executemany(
    "INSERT INTO PEOPLE (first_name, last_name, state) VALUES (?, ?, ?)",
    [("Benjamin", "Franklin", "Pennsylvania"), ("John", "Doe",
                                                "California")])
c.execute(
    "CREATE TABLE IF NOT EXISTS townspeople (id INTEGER NOT NULL PRIMARY "
    "KEY, first_name VARCHAR(100), last_name VARCHAR(100), victories "
    "FLOAT, accolades FLOAT, triumphs FLOAT)")
c.executemany(
    "INSERT INTO townspeople (first_name, last_name, victories, "
    "accolades, triumphs) VALUES (?, ?, ?, ?, ?)",
    [("George", "Washington", 20.00,
      1331241.321342132321324589798264627463827647382647382643874,
      9007199254740991.0),
     ("John", "Adams", -19.95,
      1331241321342132321324589798264627463827647382647382643874.0,
      9007199254740992.0)])
c.execute("CREATE TABLE IF NOT EXISTS data (col1 INTEGER)")
c.executemany("INSERT INTO DATA VALUES (?)", [(0,), (1,), (2,)])
conn.commit()
conn.close()
