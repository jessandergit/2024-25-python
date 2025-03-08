# initialise the inputs [1,1] and set value to the first value of the sequence
n1, n2 = 1, 1
inputs = [n1, n2]
# initialise the number of fibonacci numbers that will appear & a count for the termination condition
number_of_numbers = 29
count = 2
# while the termination condition is not true:
while count < number_of_numbers:
    # set value to the next value of the sequence
    n3 = n1 + n2
    # append value to the sequence
    inputs.append(n3)
    # update previous values
    n1, n2 = n2, n3
    # increase counter so program knows when to terminate
    count += 1
#print the sequence
print(*inputs)
