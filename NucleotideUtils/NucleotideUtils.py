def reversestrand(strand):
    i = len(strand)-1
    sr = ''
    while i>=0:
        sr = sr + strand[i]
        i = i-1
    return sr
        
def complementstrand(strand):
    strant = str(strand)
    sc = ''
    for nucleotide in strand:
        sc = sc + complementnucleotide(nucleotide)
    return sc

def complementnucleotide(n):
    n = n.upper()
    if n == 'A':
        return 'T'
    elif n == 'T':
        return 'A'
    elif n == 'C':
        return 'G'
    elif n == 'G':
        return 'C'
    else:
        return 'N'