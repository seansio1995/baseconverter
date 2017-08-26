def baseConverter(num,base):
    stack=[]
    res=""
    digits="0123456789ABCDEF"
    while num > 0:
        rem=num%base
        stack.append(rem)
        num=num//base

    while stack:
        res+=digits[stack.pop()]

    return res


if __name__=="__main__":
    print(baseConverter(120,12))
