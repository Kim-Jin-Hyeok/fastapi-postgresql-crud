def solution(x, n):
    answer = []

    for i in range(n):
        answer[i] = x + (x*i)

    return answer