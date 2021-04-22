# 숫자인 num을 인자로 넘겨주면, 뒤집은 모양이 num과 똑같은지 여부를 반환해주세요.

# num: 숫자
# return: true or false (뒤집은 모양이 num와 똑같은지 여부)

def same_reverse(num):
    reverse = str(num)[::-1]

    if str(num) == reverse:
        return True
    else:
        return False