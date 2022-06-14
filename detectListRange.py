# Function that detects ranges from a given list
def detect_ranges(L):
    sorted_L = sorted(L)
    endSequence = 0
    startSequence = 0
    result=[]
    for i in range(1,len(sorted_L)):
        if sorted_L[i-1] == sorted_L[i]-1:
            endSequence=i
            # in case of that last element comes with range
            if i+1==len(sorted_L):
                result.append((sorted_L[startSequence], sorted_L[endSequence]+1))
        else:
            if startSequence==endSequence:
                result.append(sorted_L[startSequence])
            else:
                result.append((sorted_L[startSequence], sorted_L[endSequence]+1))
            startSequence = endSequence = i
            # in case of that last element comes alone
            if i+1==len(sorted_L):
                 result.append(sorted_L[-1])         
    return result
