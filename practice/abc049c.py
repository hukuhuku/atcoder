S = input()

str_dict = {"dream":5,"dreamer":7,"erase":5,"eraser":6}

count = 0
while count < 4:
    for key, value in str_dict.items():
        count += 1
        if key == (S[-value:]):
            S = S[:-value]
            count = 0

if S == "":
    print("YES")
else:
    print("NO")
  