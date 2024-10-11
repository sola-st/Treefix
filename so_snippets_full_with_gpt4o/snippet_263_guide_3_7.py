import pandas as pd # pragma: no cover
from IPython.display import display # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
from l3.Runtime import _l_
def display_all(df):
   _l_(15148)

   with pd.option_context('display.max_rows',1000):
      _l_(15147)

      with pd.option_context('display.max_columns',1000):
         _l_(15146)

         display(df)
         _l_(15145)

