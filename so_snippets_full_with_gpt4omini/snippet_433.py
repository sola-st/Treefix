# Extracted from https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
#First, here's  a pure list version
my_sortLambdaLst = [lambda x,y:cmp(x[0], y[0]), lambda x,y:cmp(x[1], y[1])]
def multi_attribute_sort(x,y):
    r = 0
    for l in my_sortLambdaLst:
        r = l(x,y)
        if r!=0: return r #keep looping till you see a difference
    return r

Lst = [(4, 2.0), (4, 0.01), (4, 0.9), (4, 0.999),(4, 0.2), (1, 2.0), (1, 0.01), (1, 0.9), (1, 0.999), (1, 0.2) ]
Lst.sort(lambda x,y:multi_attribute_sort(x,y)) #The Lambda of the Lambda
for rec in Lst: print str(rec)

class probe:
    def __init__(self, group, score):
        self.group = group
        self.score = score
        self.rank =-1
    def set_rank(self, r):
        self.rank = r
    def __str__(self):
        return '\t'.join([str(self.group), str(self.score), str(self.rank)]) 


def RankLst(inLst, group_lambda= lambda x:x.group, sortLambdaLst = [lambda x,y:cmp(x.group, y.group), lambda x,y:cmp(x.score, y.score)], SetRank_Lambda = lambda x, rank:x.set_rank(rank)):
    #Inner function is the only way (I could think of) to pass the sortLambdaLst into a sort function
    def multi_attribute_sort(x,y):
        r = 0
        for l in sortLambdaLst:
            r = l(x,y)
            if r!=0: return r #keep looping till you see a difference
        return r

    inLst.sort(lambda x,y:multi_attribute_sort(x,y))
    #Now Rank your probes
    rank = 0
    last_group = group_lambda(inLst[0])
    for i in range(len(inLst)):
        rec = inLst[i]
        group = group_lambda(rec)
        if last_group == group: 
            rank+=1
        else:
            rank=1
            last_group = group
        SetRank_Lambda(inLst[i], rank) #This is pure evil!! The lambda purists are gnashing their teeth

Lst = [probe(4, 2.0), probe(4, 0.01), probe(4, 0.9), probe(4, 0.999), probe(4, 0.2), probe(1, 2.0), probe(1, 0.01), probe(1, 0.9), probe(1, 0.999), probe(1, 0.2) ]

RankLst(Lst, group_lambda= lambda x:x.group, sortLambdaLst = [lambda x,y:cmp(x.group, y.group), lambda x,y:cmp(x.score, y.score)], SetRank_Lambda = lambda x, rank:x.set_rank(rank))
print '\t'.join(['group', 'score', 'rank']) 
for r in Lst: print r

