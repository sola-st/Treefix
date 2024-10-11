# Extracted from https://stackoverflow.com/questions/29763620/how-to-select-all-columns-except-one-in-pandas
df[map(lambda x :x not in ['b'], list(df.columns))]

import pandas
import numpy as np
df = pd.DataFrame(np.random.rand(4,4), columns = list('abcd'))
df

       a           b           c           d
0   0.774951    0.079351    0.118437    0.735799
1   0.615547    0.203062    0.437672    0.912781
2   0.804140    0.708514    0.156943    0.104416
3   0.226051    0.641862    0.739839    0.434230

df[map(lambda x :x not in ['b'], list(df.columns))]

        a          c          d
0   0.774951    0.118437    0.735799
1   0.615547    0.437672    0.912781
2   0.804140    0.156943    0.104416
3   0.226051    0.739839    0.434230

