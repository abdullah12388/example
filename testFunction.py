def PlusMinus(text):
    filter_plus = text.replace('plus','+')
    filter_minus = filter_plus.replace('minus','-')
    return filter_minus

x = PlusMinus('minusplusplusminusminusplusplusminusminusplusplusminusminusplusplusminusminusplusplusminusminusplusminusminusplusplusminusminusplusplus')
print(x)