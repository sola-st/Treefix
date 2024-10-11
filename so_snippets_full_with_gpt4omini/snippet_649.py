# Extracted from https://stackoverflow.com/questions/27236275/what-does-valueerror-cannot-reindex-from-a-duplicate-axis-mean
df_temp['REMARK_TYPE'] = df.REMARK.apply(lambda v: 1 if str(v)!='nan' else 0)

----> 1 df_temp['REMARK_TYPE'] = df.REMARK.apply(lambda v: 1 if str(v)!='nan' else 0)

   2417         else:
   2418             # set column
-> 2419             self._set_item(key, value)
   2420 
   2421     def _setitem_slice(self, key, value):

   2483 
   2484         self._ensure_valid_index(value)
-> 2485         value = self._sanitize_column(key, value)
   2486         NDFrame._set_item(self, key, value)
   2487 

   2633 
   2634         if isinstance(value, Series):
-> 2635             value = reindexer(value)
   2636 
   2637         elif isinstance(value, DataFrame):

   2625                     # duplicate axis
   2626                     if not value.index.is_unique:
-> 2627                         raise e
   2628 
   2629                     # other

ValueError: cannot reindex from a duplicate axis

df_temp['REMARK_TYPE'] = df_temp.REMARK.apply(lambda v: 1 if str(v)!='nan' else 0)

