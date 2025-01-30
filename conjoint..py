def som_dij(n):
    return sum(int(digit) for digit in str(n))

def conjoin(s_1, s_2):
    while s_1 != s_2 :
        if s_1 < s_2 :
         s_1 = s_1+som_dij(s_1)
        else :
         s_2 = s_2+som_dij(s_2)
    return s_2