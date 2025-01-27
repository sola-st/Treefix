# Extracted from https://stackoverflow.com/questions/19913659/pandas-conditional-creation-of-a-series-dataframe-column
df.case_when(
    df.col1 == "Z",  # condition
    "green",         # value if True
    "red",           # value if False
    column_name = "color"
    )

  Type Set  color
1    A   Z  green
2    B   Z  green
3    B   X    red
4    C   Y    red

df.case_when(
    df.Set.eq('Z') & df.Type.eq('A'), 'yellow', # condition, result
    df.Set.eq('Z') & df.Type.eq('B'), 'blue',   # condition, result
    df.Type.eq('B'), 'purple',                  # condition, result
    'black',              # default if none of the conditions evaluate to True
    column_name = 'color'  
)
  Type  Set   color
1    A   Z  yellow
2    B   Z    blue
3    B   X  purple
4    C   Y   black

