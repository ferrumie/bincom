def recSearch(arr, ind, r, x):
    """
    A recursive function to search for a number given
    by user from the list of numbers present
    """
    if r < ind:
        return -1
    if arr[ind] == x:
        return ind
    if arr[r] == x:
        return r
    return recSearch(arr, ind+1, r-1, x)


# Driver Code
arr = [12, 34, 54, 2, 3, 4, 5, 98, 102]  # list of numbers
n = len(arr)
x = input("enter a number\n")
index = recSearch(arr, 0, n-1, int(x))
if index != -1:
    print("Element", int(x), "is present at index %d" % (index))
else:
    print("Element %d is not present" % (int(x)))
