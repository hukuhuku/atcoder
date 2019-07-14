#失恋してメンタル死んでるのでコードもシンデマス
 
dic = {}
key = []
item = []
res_flag = True

for i in range(3):
    a,b = map(int,input().split())
    dic[a] = b
    key.append(a)
    item.append(b)
 
for i in key:
    flag = True
    tmp_key = key
    tmp_item = item
    
    a = i
    while flag:
        if a in key:
        	a = dic[a]
            tmp_key.remove(a)
            tmp_item.remove(dic[a])
            
        else:
            flag = False
        
    if len(tmp_item) == 0 and len(tmp_key) == 0:
        res = "YES"
        res_flag = False

if res_flag:
    res = "NO"
    
    print(res)