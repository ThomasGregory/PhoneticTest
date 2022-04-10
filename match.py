import phonetics as p

def match(a, b):
    if a == b: # return early if exactly the same, to save us work!
        return True
    elif a[1] != b[1]: # first letter should match
        return False
    else:
        return p.dmetaphone(a) == p.dmetaphone(b)

def match_list(names):
    # names should be a list of tuples of (name, id) like [("dog", 21), ("cat", 5)]
    merged = {}
    for n, i in names:
        k = n if n in merged else next((n2 for n2 in merged.keys() if match(n2, n)), n)
        merged[k] = merged.get(k, []) + [i]
    return merged