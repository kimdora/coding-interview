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
            # 끝에 문자 처리
            if i == len(s) - 2:
                charArray.append(s[i] + str(cnt))
        elif s[i] != s[i + 1]:
            charArray.append(s[i] + str(cnt))
            cnt = 1
            if i == len(s) - 2:
                charArray.append(s[i + 1] + str(cnt))
                
    # 리스트 -> 문자열
    charArray = ''.join(charArray)

    if len(charArray) > len(s):
        return s
    else:
        return charArray

if __name__ == '__main__':
    # Write your test cases here
    testcase1 = "aabccccaaa"
    testcase2 = "ababb" # < "a1b1a1b2"
    testcase3 = "zzxxccvvbb" 

    assert compress(testcase1) == "a2b1c4a3"
    assert compress(testcase2) == "ababb"
    assert compress(testcase3) == "z2x2c2v2b2"
