# String 형인 str 인자에서 중복되지 않은 알파벳으로 이루어진 제일 긴 단어의 길이를 반환해주세요.

def get_len_of_str(s):
    word = ""
    lst = []
    for string in s:
        if string not in word:
            word += string
        else:
            word = string
        lst.append(word)

    result = 0
    for i in lst:
        if len(i) > result:
            result = len(i)

    return result