# i represents the first two digits，j represents the last two digits,k represents the license number
for i in range(10):
    for j in range(10):   
        # Are the first two digits and last two digits the same?
        if i != j:
            # The license number is 4 digits
            k = 1000 * i + 100 * i + 10 * j + j
            # Check if k the square of some number
            for temp in range(31, 100):
                if temp * temp == k:
                    print("License Number is: ", k)