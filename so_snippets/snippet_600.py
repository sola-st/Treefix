# Extracted from https://stackoverflow.com/questions/22219004/how-to-group-dataframe-rows-into-list-in-pandas-groupby
 L = ['A','A','B','B','B','C']
 N = [1,2,5,5,4,6]

 import pandas as pd
 df = pd.DataFrame(zip(L,N),columns = list('LN'))


 groups = df.groupby(df.L)

 groups.groups
      {'A': [0, 1], 'B': [2, 3, 4], 'C': [5]}

 groups.get_group('A')

     L  N
  0  A  1
  1  A  2

  groups.get_group('B')

     L  N
  2  B  5
  3  B  5
  4  B  4

