def all_variants(text):
    for x in range(len(text)):
        for y in range(len(text)):
            if x + y >= (len(text)):
                continue
            yield text[y:x + y + 1]
a = all_variants("abc")
for i in a:
    print(i)