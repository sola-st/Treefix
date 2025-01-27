# Extracted from https://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas
frame.apply(np.sqrt)
Out[102]: 
               b         d         e
Utah         NaN  1.435159       NaN
Ohio    1.098164  0.510594  0.729748
Texas        NaN  0.456436  0.697337
Oregon  0.359079       NaN       NaN

frame.applymap(np.sqrt)
Out[103]: 
               b         d         e
Utah         NaN  1.435159       NaN
Ohio    1.098164  0.510594  0.729748
Texas        NaN  0.456436  0.697337
Oregon  0.359079       NaN       NaN

