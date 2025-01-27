# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH 40682
# Test for the is_named_tuple() function
# Placed here due to its usage of sqlalchemy

from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
)

BaseModel = declarative_base()

class Test(BaseModel):
    __tablename__ = "test_frame"
    id = Column(Integer, primary_key=True)
    string_column = Column(String(50))

BaseModel.metadata.create_all(self.conn)
Session = sessionmaker(bind=self.conn)
with Session() as session:
    df = DataFrame({"id": [0, 1], "string_column": ["hello", "world"]})
    assert (
        df.to_sql("test_frame", con=self.conn, index=False, if_exists="replace")
        == 2
    )
    session.commit()
    test_query = session.query(Test.id, Test.string_column)
    df = DataFrame(test_query)

assert list(df.columns) == ["id", "string_column"]
