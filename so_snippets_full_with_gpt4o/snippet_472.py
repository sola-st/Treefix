# Extracted from https://stackoverflow.com/questions/13295735/how-to-replace-nan-values-by-zeroes-in-a-column-of-a-pandas-dataframe
d1 = {"Col1" : ['A', 'B', 'C'],
     "fruits": ['Avocado', 'Banana', 'NaN']}
d1= pd.DataFrame(d1)

output:

Col1    fruits
0   A   Avocado
1   B   Banana
2   C   NaN


d1.loc[ d1.Col1=='C', 'fruits' ] =  'Carrot'


output:

Col1    fruits
0   A   Avocado
1   B   Banana
2   C   Carrot

