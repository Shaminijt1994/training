def bubble_sort(numbers):
    size_of_array = len(numbers)
    for i in range(size_of_array):
        for j in range(i+1,size_of_array):
            if numbers[i]>numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers
numbers= []
a = int(input("Enter the numbers:"))
for i in range(0,a):
    b= int(input())
    numbers.append(b)
sort = bubble_sort(numbers)
print(sort)


