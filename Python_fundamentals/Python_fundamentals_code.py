# Task 1: Display Fibonacci Series up to 10 terms
def fibonacci_series(n):
    series = [0, 1]
    for i in range(2, n):
        next_term = series[-1] + series[-2]
        series.append(next_term)
    return series

# Task 2: Display numbers at the odd indices of a list
def odd_indices_numbers(lst):
    return lst[1::2]

# Task 3: Print a list in reverse order
def reverse_list(lst):
    return lst[::-1]

# Task 4: Count the number of different words in the given text
text = """
ChatGPT has created this text to provide tips on creating interesting paragraphs. 
First, start with a clear topic sentence that introduces the main idea. 
Then, support the topic sentence with specific details, examples, and evidence.
Vary the sentence length and structure to keep the reader engaged.
Finally, end with a strong concluding sentence that summarizes the main points.
Remember, practice makes perfect!
"""

def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

# Task 5: Write a function that counts vowels in a word
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in word if char in vowels)
    return count

# Task 6: Iterate through and print animals in all caps
animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for animal in animals:
    print(animal.upper())

# Task 7: Iterate from 1 to 15, printing whether the number is odd or even
for number in range(1, 16):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# Task 8: Take two integers as input and return their sum
def add_two_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    return result

# Examples
print("Task 1: Fibonacci Series up to 10 terms:", fibonacci_series(10))
print("Task 2: Numbers at Odd Indices of a List:", odd_indices_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("Task 3: List in Reverse Order:", reverse_list([1, 2, 3, 4, 5]))
print("Task 4: Number of Different Words in Text:", count_unique_words(text))
print("Task 5: Number of Vowels in 'GitHub':", count_vowels("GitHub"))
print("Task 8: Sum of Two Numbers:", add_two_numbers())
