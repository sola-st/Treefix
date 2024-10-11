# Extracted from https://stackoverflow.com/questions/15891038/change-column-type-in-pandas
In [40]: df = pd.DataFrame(
    ...:     {
    ...:         "a": pd.Series([1, 2, 3], dtype=np.dtype("int32")),
    ...:         "b": pd.Series(["x", "y", "z"], dtype=np.dtype("O")),
    ...:         "c": pd.Series([True, False, np.nan], dtype=np.dtype("O")),
    ...:         "d": pd.Series(["h", "i", np.nan], dtype=np.dtype("O")),
    ...:         "e": pd.Series([10, np.nan, 20], dtype=np.dtype("float")),
    ...:         "f": pd.Series([np.nan, 100.5, 200], dtype=np.dtype("float")),
    ...:     }
    ...: )

In [41]: dff = df.copy()

In [42]: df 
Out[42]: 
   a  b      c    d     e      f
0  1  x   True    h  10.0    NaN
1  2  y  False    i   NaN  100.5
2  3  z    NaN  NaN  20.0  200.0

In [43]: df.dtypes
Out[43]: 
a      int32
b     object
c     object
d     object
e    float64
f    float64
dtype: object

In [44]: df = df.convert_dtypes()

In [45]: df.dtypes
Out[45]: 
a      Int32
b     string
c    boolean
d     string
e      Int64
f    float64
dtype: object

In [46]: dff = dff.convert_dtypes(convert_boolean = False)

In [47]: dff.dtypes
Out[47]: 
a      Int32
b     string
c     object
d     string
e      Int64
f    float64
dtype: object

