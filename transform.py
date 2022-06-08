'''function that gets two strings as parameters and returns a list of integers using split method and map function. The function should split the strings into words, and convert these words to integers. This should give two lists of integers. Then the function should return a list whose elements are multiplication of two integers in the respective positions in the lists. For example transform("1 5 3", "2 6 -1") should return the list of integers [2, 30, -3].
assuming that the two input strings are in correct format.'''

def transform(s1, s2):
    l1 = list(s1.split())
    l2 = list(s2.split())
    int_l1=[]
    int_l2=[]
    for i in range(len(l1)):
        int_l1.append(int(l1[i]))
    for i in range(len(l2)):
        int_l2.append(int(l2[i]))
    return list(map(lambda x,y : x*y, int_l1, int_l2))
