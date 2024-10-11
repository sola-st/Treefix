# Extracted from https://stackoverflow.com/questions/20763012/creating-a-pandas-dataframe-from-a-numpy-array-how-do-i-specify-the-index-colum
def csvDf(dat,**kwargs): 
  from numpy import array
  data = array(dat)
  if data is None or len(data)==0 or len(data[0])==0:
    return None
  else:
    return pd.DataFrame(data[1:,1:],index=data[1:,0],columns=data[0,1:],**kwargs)

data = [['','a','b','c'],['row1','row1cola','row1colb','row1colc'],
     ['row2','row2cola','row2colb','row2colc'],['row3','row3cola','row3colb','row3colc']]
csvDf(data)

In [61]: csvDf(data)
Out[61]:
             a         b         c
row1  row1cola  row1colb  row1colc
row2  row2cola  row2colb  row2colc
row3  row3cola  row3colb  row3colc

