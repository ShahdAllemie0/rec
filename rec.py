def rec( numbers):
        total = 0
        for element in numbers:
            if type(element) == list:
                total += rec(element)
            else:
                total += element
        return total
numbers = [
    [1, 2, 3, 4],
    [3, 6, [5, 6], 8, 2,[2, 4], 9],
    [4, 2, [6, 7, [2, 6, 1]]]
] 

print(rec(numbers))
