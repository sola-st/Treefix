# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
from l3.Runtime import _l_
def display_all(df):
   _l_(2765)

   with pd.option_context('display.max_rows',1000):
      _l_(2764)

      with pd.option_context('display.max_columns',1000):
         _l_(2763)

         display(df)
         _l_(2762)

