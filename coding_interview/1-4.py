def is_palindrome(s: str) -> bool:
    """
    Given a string, write a function to check if it is a permutation of a
    palindrome. A palindrome is a word or phrase that is the same forwards and
    backwards. A permutation is a rearrangement of letters.
    """
    s = s.replace(" ", "")
    s = s.lower()
    for i in range(len(s) // 2):
        num = (len(s) - 1) - i
        if s[i] != s[num]:
            return False
    return True

if __name__ == '__main__':
    # Write your test cases here
    assert is_palindrome("aba") == True
    assert is_palindrome("abc") == False
    assert is_palindrome("a") == True
    assert is_palindrome("Taco cat") == True
