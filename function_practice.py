# Python function called max_num()to find the maximum of three numbers.

def max_num(x, y, z):
    max_num = max(x, y, z)
    print(max_num)

max_num(18, 3, 2)

# Python function called mult_list() to multiply all the numbers in a list.

def mult_list(nums):
    total = nums[0]
    if len(nums) == 0:
        return 0
    else:
        for num in nums:
            total = total * num 
    print(total)

mult_list([1, 2, 6])

# Python function called rev_string() to reverse a string.

def rev_string(string):
    reverse = string[::-1]
    print(reverse)

rev_string("hello racecar")

# Python function called num_within() to check whether a number falls in a given range.

def num_within(num, range_start, range_end):
    return range_start <= num <= range_end
print(num_within(13, 12, 14))

# Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
    if n <= 0:
        return
    elif n == 1:
        print(n)
        return [1]
    else:
        prev_row = pascal(n - 1)
        row = [1] * n
        for i in range(1, n - 1):
            row[i] = prev_row[i - 1] + prev_row[i]
        print(" ".join(map(str, row)))
        return row
    
pascal(5)