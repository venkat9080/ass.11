# 1.Write a program to find all pairs of an integer array whose sum is equal to a given number?
def find_pairs(array, target_sum):
    pairs = []
    num_dict = {}
    
    for num in array:
        complement = target_sum - num
        if complement in num_dict:
            pairs.append((complement, num))
        num_dict[num] = True
    
    return pairs


# Example usage:
array = [2, 4, 6, 5, 9, 1, 3, 7]
target_sum = 10

pairs = find_pairs(array, target_sum)

if len(pairs) > 0:
    print(f"The pairs in the array that sum up to {target_sum} are:")
    for pair in pairs:
        print(pair)
else:
    print(f"No pairs found in the array that sum up to {target_sum}.")

#2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def reverse_array(array):
    start = 0
    end = len(array) - 1
    
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


# Example usage:
array = [1, 2, 3, 4, 5]
print("Original array:", array)

reverse_array(array)
print("Reversed array:", array)

#3.Write a program to check if two strings are a rotation of each other?
def are_rotations(string1, string2):
    if len(string1) != len(string2):
        return False
    
    # Concatenate string1 to itself
    concatenated = string1 + string1
    
    if string2 in concatenated:
        return True
    else:
        return False


# Example usage:
string1 = "hello"
string2 = "lohel"

if are_rotations(string1, string2):
    print(f"{string1} and {string2} are rotations of each other.")
else:
    print(f"{string1} and {string2} are not rotations of each other.")

#//---4. Write a program to print the first non-repeated character from a string?
def first_non_repeated_char(string):
    char_count = {}
    
    # Count the occurrences of each character
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first non-repeated character
    for char in string:
        if char_count[char] == 1:
            return char
    
    return None  # No non-repeated character found


# Example usage:
string = "aabccdef"

result = first_non_repeated_char(string)

if result is not None:
    print(f"The first non-repeated character in '{string}' is '{result}'.")
else:
    print(f"There is no non-repeated character in '{string}'.")

#5. Read about the Tower of Hanoi algorithm. Write a program to implement it
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source)


# Example usage:
num_disks = 3
tower_of_hanoi(num_disks, 'A', 'C', 'B')

#6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
def postfix_to_prefix(expression):
    stack = []

    # Iterate through the expression
    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(char + operand1 + operand2)

    # The final result will be on the top of the stack
    return stack[-1]


# Example usage:
postfix_expr = "ab+c*"

prefix_expr = postfix_to_prefix(postfix_expr)

print("Postfix expression:", postfix_expr)
print("Prefix expression:", prefix_expr)

# 7. Write a program to convert prefix expression to infix expression.
def prefix_to_infix(expression):
    stack = []

    # Iterate through the expression in reverse order
    for char in reversed(expression):
        if char.isalnum():
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append("(" + operand1 + char + operand2 + ")")

    # The final result will be on the top of the stack
    return stack[-1]


# Example usage:
prefix_expr = "*+AB-CD"

infix_expr = prefix_to_infix(prefix_expr)

print("Prefix expression:", prefix_expr)
print("Infix expression:", infix_expr)

#8. Write a program to check if all the brackets are closed in a given code snippet.
def check_brackets(code):
    stack = []

    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            opening_bracket = stack.pop()
            corresponding_closing_bracket = opening_brackets[closing_brackets.index(char)]
            if opening_bracket != corresponding_closing_bracket:
                return False

    return len(stack) == 0


# Example usage:
code_snippet = """
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
"""

if check_brackets(code_snippet):
    print("All brackets in the code snippet are closed.")
else:
    print("Some brackets in the code snippet are not closed.")

#9. Write a program to reverse a stack
def reverse_stack(stack):
    if not stack:
        return

    # Remove the top element from the stack
    top = stack.pop()

    # Reverse the remaining stack
    reverse_stack(stack)

    # Insert the top element at the bottom of the reversed stack
    insert_at_bottom(stack, top)


def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return

    top = stack.pop()

    insert_at_bottom(stack, item)

    stack.append(top)


# Example usage:
stack = [1, 2, 3, 4, 5]
print("Original stack:", stack)

reverse_stack(stack)
print("Reversed stack:", stack)

#10. Write a program to find the smallest number using a stack.
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]


# Example usage:
stack = MinStack()

stack.push(5)
stack.push(2)
stack.push(7)
stack.push(1)

smallest = stack.get_min()
print("Smallest number:", smallest)

