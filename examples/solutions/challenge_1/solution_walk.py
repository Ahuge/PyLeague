def frames(s):
    def x(i):
        try: return s[i]
        except: return ""
    i = -1
    while x(i):
        if x(i) == "]" and x(i-1).isdigit():
            j = i-1
            while x(j-1).isdigit(): j -= 1
            if x(j-1) == "-" and x(j-2).isdigit():
                k = j-1
                while x(k-1).isdigit(): k -= 1
                if x(k-1) == "[":
                    return int(s[j:i])-int(s[k:j-1])+1
        i -= 1
    return 0
