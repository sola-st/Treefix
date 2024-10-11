# Extracted from https://stackoverflow.com/questions/53645882/pandas-merging-101
import pandas as pd
import numpy as np

np.random.seed([3, 14])
left = pd.DataFrame(data={'value': np.random.randn(4)}, 
                    index=['A', 'B', 'C', 'D'])    
right = pd.DataFrame(data={'value': np.random.randn(4)},  
                     index=['B', 'D', 'E', 'F'])
left.index.name = right.index.name = 'idxkey'

left
           value
idxkey          
A      -0.602923
B      -0.402655
C       0.302329
D      -0.524349

right
 
           value
idxkey          
B       0.543843
D       0.013135
E      -0.326498
F       1.385076

left.merge(right, left_index=True, right_index=True)

         value_x   value_y
idxkey                    
B      -0.402655  0.543843
D      -0.524349  0.013135

 left.join(right, how='inner', lsuffix='_x', rsuffix='_y')

          value_x   value_y
 idxkey                    
 B      -0.402655  0.543843
 D      -0.524349  0.013135

 left.join(right)
 ValueError: columns overlap but no suffix specified: Index(['value'], dtype='object')

 left.rename(columns={'value':'leftvalue'}).join(right, how='inner')

         leftvalue     value
 idxkey                     
 B       -0.402655  0.543843
 D       -0.524349  0.013135

 pd.concat([left, right], axis=1, sort=False, join='inner')

            value     value
 idxkey                    
 B      -0.402655  0.543843
 D      -0.524349  0.013135

right2 = right.reset_index().rename({'idxkey' : 'colkey'}, axis=1)
right2
 
  colkey     value
0      B  0.543843
1      D  0.013135
2      E -0.326498
3      F  1.385076

left.merge(right2, left_index=True, right_on='colkey')

    value_x colkey   value_y
0 -0.402655      B  0.543843
1 -0.524349      D  0.013135

left.merge(right, on='idxkey')

         value_x   value_y
idxkey                    
B      -0.402655  0.543843
D      -0.524349  0.013135

left.merge(right2, left_on='idxkey', right_on='colkey')

    value_x colkey   value_y
0 -0.402655      B  0.543843
1 -0.524349      D  0.013135

