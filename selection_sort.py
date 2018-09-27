def selection_Sort(nums): #takes in one array to be sorted.
    for i in range(len(nums)-1):
        index = i
        for j in range(i+1,len(nums),1):
            if nums[j]<nums[index]:
                index = j
# we look for the smallest item on every iteration coz we want to sort in ascending order.
        if index !=i:
            swap(nums, index,i)
    return nums

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = temp

if __name__ =="__main__":
    nums = [-1,-3,-2,0]
    print(selection_Sort(nums))
 
