def is_permutation(s1: str, s2: str) -> bool:
    """
    Given two strings, write a method to decide if one is a permutation of the
    other.
    """
    if len(s1) != len(s2):
        return False
    else:
        s1 = sorted(s1)
        s2 = sorted(s2)
        if s1 == s2:
            return True
        else:
            return False

if __name__ == '__main__':
    # Write your test cases here
    
    assert is_permutation("abcde", "abdec") == True
    assert is_permutation("abcde", "abd") == False
    assert is_permutation("abcde", "dsfav") == False
    assert is_permutation("abcde", "abbcde") == False