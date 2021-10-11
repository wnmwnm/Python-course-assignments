def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    length = 0
    for char in dna:
        length = length + 1
    return length


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    if get_length(dna1) > get_length(dna2):
        return True
    else:
        return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    
    num_nuc = 0
    for char in dna:
        if nucleotide == char:
            num_nuc = num_nuc + 1
        else:
            num_nuc = num_nuc
    return num_nuc


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    
    if dna1.find(dna2) > -1:
        return True
    else:
        return False

def is_valid_sequence(dna):
    """(str) -> bool

    Return True if and only if the DNA sequence is valid.
    
    >>>is_valid_sequence('ATCGTAG')
    True
    >>>is_valid_sequence('ATCGBTAG')    
    False
    """
    
    invalid = 0  
    for char in dna:
        if char in "ATCG":
            invalid = invalid
        else:
            invalid = invalid + 1
    if invalid > 0:
        return False
    else:
        return True

def insert_sequence(dna1, dna2, index):
    """(str, str, int) -> str

    Return the DNA sequence by inserting dna2 into dna1 at the given index.

    >>>insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>>insert_sequence('GCATCG', 'AT', 0)
    'ATGCATCG'
    """
    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nuc):
    """(str) -> str

    Return nuc's complement.
    
    >>>get_complement('A')
    'T'
    >>>get_complement('G')
    'C'
    >>>get_complement('W')
    'Not a nucleotide.'
    """
    if nuc == 'A':
        return 'T'
    elif nuc == 'T':
        return 'A'
    elif nuc == 'G':
        return 'C'
    elif nuc == 'C':
        return 'G'
    else:
        return 'Not a nucleotide.'

def get_complementary_sequence(seq):
    """(str) -> str

    Return the complementary sequence of seq.
    
    >>>get_complementary_sequence('AT')
    'TA'
    >>>get_complementary_sequence('CGATGCAT')
    'GCTACGTA'
    """
    
    comp_seq = ''
    
    for char in seq:
        comp_seq = comp_seq + get_complement(char)
    return comp_seq








    
