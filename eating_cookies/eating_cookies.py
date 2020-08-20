'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    values = {
        0:1, 
        1:1, 
        2:2, 
    }

    if n == 0:
        # because that is the last way it can eat the cookie, meaning all cookies have been eaten
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    for i in range(3, n+1):
        # we store in a cache the value of the combination of ways cookies can be eaten, 
        values[i] = values[i-1] + values[i-2] + values[i-3]
    return values[i]
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
