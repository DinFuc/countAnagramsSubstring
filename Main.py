def chuyen(s):
    if len(s)>1:
        s = s[1:] + s[0]
    return s
def chuyen2(s):
    if len(s)>1:
        s = s[len(s)-1] + s[:len(s)-1]
    return s
def countAnagramsSubstring(s):
    str = {}
    d = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if s[i:j] not in str:
                if chuyen(s[i:j]) in str:
                    str[chuyen(s[i:j])] += 1
                    continue
                if chuyen2(s[i:j]) in str:
                    str[chuyen2(s[i:j])] += 1
                    continue
                str[s[i:j]] = 1
            else:
                str[s[i:j]] += 1
    for i in str.values():
        d += i*(i-1)/2
    return d
