dnaToRnaDict = {'A':'A', 'T':'U', 'G':'G', 'C':'C'}

def dnaToRna(dnaStrand):
    rnaStrand = ''
    for nt in dnaStrand:
        rnaStrand = rnaStrand + dnaToRnaDict[nt]
    return rnaStrand