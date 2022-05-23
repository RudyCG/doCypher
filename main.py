def pubkey(p, g ,x):
    key = ZZ(power_mod(g,x,p))
    return key
pubkey(11,2,7)