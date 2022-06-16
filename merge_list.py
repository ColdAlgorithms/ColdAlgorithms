# function which merges and sorts two lists in one
def merge(L1, L2):
    return sorted(set(sorted(L1)+sorted(L2)))
