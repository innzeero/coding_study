# --url--
# https://www.acmicpc.net/problem/10952

# --title--
# 10952번: A+B - 5

# --problem_description--
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# --problem_input--
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 입력의 마지막에는 0 두 개가 들어온다.

# --problem_output--
# 각 테스트 케이스마다 A+B를 출력한다.

# res = 1
# while res != 0:
#     a, b = map(int, input().split())
#     res = a+b
#     if res != 0 :
#         print(res)
#     else :
#         pass


# while문의 무한루프 사용시 코드가 더 깔끔하다
while True :
    a, b = map(int, input().split())
    if a ==0 and b == 0:
        break
    else:
        print(a+b)