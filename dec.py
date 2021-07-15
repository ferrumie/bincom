import random

# Generate 4 random digits
# Function to create the
# random binary string


def rand_key(p):

    # Variable to store the
    # string
    key1 = ""

    # Loop to find the string
    # of desired length
    for i in range(p):

        # randint function to generate
        # 0, 1 randomly and converting
        # the result into str
        temp = str(random.randint(0, 1))

        # Concatenatin the random 0, 1
        # to the final result
        key1 += temp

        # convert to decimal
        decim = int(key1, 2)
    return(f"binary {key1}, decimal {decim}")


digits = rand_key(4)
print(digits)
