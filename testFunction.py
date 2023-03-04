def Solution(s):
    s = s.replace('plus','+')
    s = s.replace('minus','-')
    return s

_str = 'minusplusplusminusminusplusplusminusminusplusplusminusminusplusplusminusminusplusplusminusminusplusminusminusplusplusminusminusplusplus'
_str2 = 'minusplusminusplusminusplusminusplusminusplusminusplusminusplusminusplusminusplusminusplusminusplusminusplusminusplusminusplusminusplus'
print(Solution(_str))
print(Solution(_str2))