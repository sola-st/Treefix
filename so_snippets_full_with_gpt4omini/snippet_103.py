# Extracted from https://stackoverflow.com/questions/11285613/selecting-multiple-columns-in-a-pandas-dataframe
import pandas as pd
df = pd.DataFrame([[1, 2,5], [5,4, 5], [7,7, 8], [7,6,9]],
                  index=['Jane', 'Peter','Alex','Ann'],
                  columns=['Test_1', 'Test_2', 'Test_3'])

       Test_1  Test_2  Test_3
Jane        1       2       5
Peter       5       4       5
Alex        7       7       8
Ann         7       6       9

df[['Test_1', 'Test_3']]

       Test_1  Test_3
Jane        1       5
Peter       5       5
Alex        7       8
Ann         7       9

df.Test_2

Jane     2
Peter    4
Alex     7
Ann      6

df.loc[:, 'Test_1':'Test_3']

       Test_1  Test_2  Test_3
Jane        1       2       5
Peter       5       4       5
Alex        7       7       8
Ann         7       6       9

df.loc[['Peter', 'Ann'], ['Test_1', 'Test_3']]

       Test_1  Test_3
Peter       5       5
Ann         7       9

