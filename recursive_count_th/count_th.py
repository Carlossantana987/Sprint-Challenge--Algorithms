'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    print(word)


    if (len(word) < 2):
        return 0
    elif (word[0:2] == 'th'):
        return 1 + count_th(word[1::])
    else:
        return 0 + count_th(word[1::])


    # if len(word) < 0:
    #     return 0
    # else:
    #     words = list(word)
    #     count_th(words -1)

