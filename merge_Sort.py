def merge_sort(nums):
    """
    divide and conquer algorithm hence recursion
    """
    if len(nums)==1:
        # if its a single item in the array, we consider the array to be sorted.
        return

    middle_index = len(nums)//2

    left_half = nums[:middle_index]
    right_half = nums[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0

    while i<len(left_half) and j<len(right_half):
        if left_half[i] < right_half[j]:
            nums[k] = left_half[j]
            i = i + 1
        else:
            nums[k] = right_half[j]
            j = j + 1
        k = k + 1

    while i<len(left_half):
        nums[k] = left_half[i]
        k = k + 1
        j = j + 1
        
if __name__ == '__main__':
    nums = [2,34,1,45,6,2]
    merge_sort(nums)
    print(nums)
