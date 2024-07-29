def Decrypt(phrase):
    decr = [ord(char) for char in phrase]
    result = []
    for i in decr:
        i -= 5
        result.append(i)

    answer = str()

    for j in result:
        answer += chr(j)

    return answer
