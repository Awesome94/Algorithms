def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(0, len(nums)-1-i, 1): #for every single iteration we consider to have one item sorted
        if nums[j] > mnums[j+1]:
            swap(nums, j, j+1)

    return nums

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

if __name__=="__main__":

    a = [2,4,1,213,4]
    print(bubble_sort(a))              
