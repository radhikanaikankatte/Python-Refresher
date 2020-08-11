def multiplier_of(number):
    def multiplier(n):
        return number * n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))