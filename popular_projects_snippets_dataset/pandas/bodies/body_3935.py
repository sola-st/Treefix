# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
data = """day,time,smoker,sum,len
Fri,Dinner,No,8.25,3.
Fri,Dinner,Yes,27.03,9
Fri,Lunch,No,3.0,1
Fri,Lunch,Yes,13.68,6
Sat,Dinner,No,139.63,45
Sat,Dinner,Yes,120.77,42
Sun,Dinner,No,180.57,57
Sun,Dinner,Yes,66.82,19
Thu,Dinner,No,3.0,1
Thu,Lunch,No,117.32,44
Thu,Lunch,Yes,51.51,17"""

df = pd.read_csv(StringIO(data)).set_index(["day", "time", "smoker"])

# it works, #2100
result = df.unstack(2)

recons = result.stack()
tm.assert_frame_equal(recons, df)
