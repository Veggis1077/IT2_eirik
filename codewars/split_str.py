def solution(s):
    for i in range(len(s)):
        a = 0
        if s[i].isalpha():
            s = s[:a] + ' ' + s[a:]
        print(s[i])
        a+=1
    return s

print(solution("helloWorld"))