def split_even_odd(number):
    even = []
    odd= []
    for n in number:
        if n % 2 ==0:
            even.append(n)
        else:
            odd.append(n)
    return even, odd #return two lists

nums = [1,2,3,4,5,6,7,8,9]
evens, odds = split_even_odd(nums)
print("Evens:",evens)
print("odd:",odds)