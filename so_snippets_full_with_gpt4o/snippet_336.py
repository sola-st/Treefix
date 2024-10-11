# Extracted from https://stackoverflow.com/questions/20461165/how-to-convert-index-of-a-pandas-dataframe-into-a-column
import pandas as pd

df = pd.DataFrame({"gi":[232,66,34,43],"ptt":[342,56,662,123]})

    gi  ptt
0  232  342
1   66   56
2   34  662
3   43  123

df.reset_index(names=['new'])

   new   gi  ptt
0    0  232  342
1    1   66   56
2    2   34  662
3    3   43  123

