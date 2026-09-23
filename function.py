#Function programs
#1.Write a function to print "Hello, World!"
def hello_world():
    print("Hello, World!")

hello_world()

#2.Write a function that takes a name and prints a greeting.
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
#3.write a function to add to numbers.
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 3))

#4.Write a function to find the square of a number.
def square(number):
    return number * number

print(square(5))

#5.Write a function to check whether a number is even or odd.
def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(7)
#6.write a function to find the maximum of two numbers.
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum(10, 20))
#7.write a function to convert Celcsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(25))
#8.write a function to calculate the area of circle.
def circle_area(radius):
    return 3.14 * radius * radius

print(circle_area(5))
#9.write a function to calculate the factorial of a number.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
#10.write a function to check whether a number is positive ,negative,zero.
def check_number(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

check_number(10)
#11.write a function to find the maximum of three  numbers.
def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(maximum(10, 25, 15))

#12.write a function to count vowels in a string.
def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count

print(count_vowels("Hello World"))
#13.write a function to reverse a string.
def reverse_string(text):
    return text[::-1]

print(reverse_string("Hello"))
#14.write a function to check whether a string is a palindrome.
def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("madam"))
#15.write a function to find the sum of all elements in a list.
def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_list([1, 2, 3, 4, 5]))
#16.write a function to find the largest element in a list.
def largest_element(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print(largest_element([10, 25, 7, 40, 15]))
#17.write a function to remove duplicate elements from a list.
def remove_duplicates(numbers):
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
#18.write a function to count how many times an element appears in a list.
def count_element(numbers, element):
    count = 0
    for number in numbers:
        if number == element:
            count += 1
    return count

print(count_element([1, 2, 2, 3, 2, 4], 2))
#19.write a function to check whether a number is prime.
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

print(is_prime(7))
#20.write a function to return all prime numbers between two numbers.
def primes_between(start, end):
    primes = []

    for number in range(start, end + 1):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                primes.append(number)

    return primes

print(primes_between(10, 30))
#21.write a function to calculate Fibonacci numbers.
def fibonacci(n):
    a, b = 0, 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

print(fibonacci(10))
#22.write a function to find the second -largest number in a list.
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]

print(second_largest([10, 20, 5, 30, 25]))
#23.write a function to sort a list without using sort().
def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

print(sort_list([5, 2, 8, 1, 3]))
#24.write a function two lists and remove duplicates.

def merge_and_remove_duplicates(list1, list2):
    result = []

    for item in list1 + list2:
        if item not in result:
            result.append(item)

    return result

print(merge_and_remove_duplicates([1, 2, 3], [2, 3, 4, 5]))
