def compress(s: str) -> str:
    """
    Implement a method to perform basic string compression using the counts of
    repeated characters. For example, the string aabcccccaaa would become
    a2b1c5a3. If the "compressed" string would not become smaller than the
    original string, your method should return the original string.
    """
    charArray = [] # 최종 문자열 저장 배열
    cnt = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            charArray.append(s[i] + str(cnt))
            cnt = 1




if __name__ == '__main__':
    # Write your test cases here
    testcase1 = "aabccccaaa"
    testcase2 = "ababb"
    testcase3 = "zzxxccvvbb" 

    assert compress(testcase1) == "a2b1c4a3"
    assert compress(testcase2) == "b1"
    assert compress(testcase3) == "z2x2c2v2b2"
