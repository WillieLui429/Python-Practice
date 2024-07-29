def Encrypt(phrase):
    encr = [ord(char) for char in phrase]
    result = []
    for i in encr:
        i += 5
        result.append(i)

    answer = str()

    for j in result:
        answer += chr(j)

    return answer
