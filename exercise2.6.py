print('Say anything!')
answer = input().lower()
def wrap_text(word, symbol):
    return "{}{}{}".format(symbol,word,symbol)

print(wrap_text(answer, '==='))
print("---" + "===" + wrap_text(answer, '###') + "===" + "---")
