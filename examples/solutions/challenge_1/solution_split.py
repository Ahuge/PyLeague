frames=lambda s:(lambda x: x[1]-x[0]+1)(map(int, s.split("[")[-1].split("]")[0].split("-")))

def frames(s, *args):
    s = s.split("[")[-1].split("]")[0].split("-")
    s,e = map(int, s)
    return e-s+1
