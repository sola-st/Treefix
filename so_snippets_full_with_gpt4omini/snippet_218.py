# Extracted from https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file
df.to_csv(file_name, encoding='utf-8', index=False)

  Color  Number
0   red     22
1  blue     10

Color,Number
red,22
blue,10

,Color,Number
0,red,22
1,blue,10

