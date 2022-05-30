'''def recsub(num):
    if num>0:
        recsub(num - 1)
    print(num)

recsub(100)

'''


def highLet(let, word):
    x = let
    if let < word[0]:
        x = word[0]
    if len(word) > 1:
        return highLet(x, word[1:])

print(highLet('a', "My test string"))

# def high_letter(n):
