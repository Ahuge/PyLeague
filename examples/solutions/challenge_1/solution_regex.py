def frames(s):
    import re
    m = re.search(r"\[(\d+\-\d+)\]", s)
    s,e=map(int,m.group(1).split("-")) if m else [-1,0]
    return e-s+1
