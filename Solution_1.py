#Decode a string problem 
def answer(s):
    forward = [chr(x) for x in range(97,123)]
    backward = [chr(x) for x in range(97,123)]
    backward.reverse()
    decoded = ""
    for c in s:
        decoded = decoded + backward[forward.index(c)]
    return decoded