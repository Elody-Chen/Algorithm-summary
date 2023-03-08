import os

# Sort Algorithm
class sortMachine:
    # Bubble Sort
    def bubbleSort(self, nums: list) -> list:
        """
        Time complexity: O(n^2)
        Spatial complexoty: O(1)
        Stable sort
        In-place
        """
        if len(nums) <= 1:
            return nums
        n = len(nums)
        for i in range(n - 1):
            flag = True
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    flag = False
                    temp = nums[j + 1]
                    nums[j + 1] = nums[j]
                    nums[j] = temp
            if flag == True:
                break

        return nums


    # Select Sort
    def selectSort(self, nums: list) -> list:
        """
        Time complexity: O(n^2)
        Spatial complexoty: O(1)
        Unstable sort
        In-place
        """
        if len(nums) <= 1:
            return nums
        n = len(nums)
        for i in range(n - 1):
            minIndex = i
            for j in range(i + 1, n):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            temp = nums[i]
            nums[i] = nums[minIndex]
            nums[minIndex] = temp

        return nums


    # Insert Sort
    def insertSort(self, nums: list) -> list:
        """
        Time complexity: O(n^2)
        Spatial complexoty: O(1)
        Stable sort
        In-place    
        """
        if len(nums) <= 1:
            return nums
        n = len(nums)
        for i in range(1, n):
            temp = nums[i]
            k = i - 1
            while k >= 0 and nums[k] > temp:
                k -= 1
            for j in range(i, k + 1, -1):
                nums[j] = nums[j - 1]
            nums[k + 1] = temp
        
        return nums


    # Quick Sort
    def quickSort(self, nums: list) -> list:
        """
        Time Complexity: O(nlogn)
        Spatial Complexity: O(logn)
        Unstable sort
        In-place
        """
        if len(nums) <= 1:
            return nums
        self.__quictSortRecursiveFun(nums, 0, len(nums) - 1)
        return nums

    def __quictSortRecursiveFun(self, nums: list, low: int, high: int):
        if low < high:
            index = self.__partition(nums, low, high)
            self.__quictSortRecursiveFun(nums, low, index - 1)
            self.__quictSortRecursiveFun(nums, index + 1, high)

    def __partition(self, nums: list, low: int, high: int) -> int:
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= pivot:
                low += 1
            nums[high] = nums[low]
        
        nums[low] = pivot

        return low


    # Merge Sort
    def mergeSort(self, nums: list) -> list:
        """
        Time Complexity: O(nlogn)
        Spatial Complexity: O(n)
        Stable sort
        Out-place
        """
        self.__mergeSortRecursiveFun(nums, 0, len(nums) - 1)
        return nums

    def __mergeSortRecursiveFun(self, nums: list, low: int, high: int):
        if low >= high:
            return
        mid = low + (high - low) // 2
        self.__mergeSortRecursiveFun(nums, low, mid)
        self.__mergeSortRecursiveFun(nums, mid + 1, high)
        temp = []
        i = low
        j = mid + 1
        # merge two sorted array
        while i <= mid and j <= high:
            if nums[j] < nums[i]:
                temp.append(nums[j])
                j += 1
            else:
                temp.append(nums[i])
                i += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= high:
            temp.append(nums[j])
            j += 1

        nums[low : high + 1] = temp



if __name__ == "__main__":
    import time
    sortCase = sortMachine()
    nums = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
    # 用nums的复制，而不用nums，因为前几个算法是原地算法，如果用nums的话会修改nums。
    print(sortCase.bubbleSort(nums.copy()))
    print(sortCase.selectSort(nums.copy()))
    print(sortCase.insertSort(nums.copy()))
    print(sortCase.quickSort(nums.copy()))
    print(sortCase.mergeSort(nums.copy()))


    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    f = open(path + "/sortTestcase.txt", encoding = "utf-8")
    s = f.read()
    f.close()
    nums = list(map(int, s.split(",")))

    sortMachineInstance = sortMachine()
    # Bubble sort
    startTime = time.time()
    sortMachineInstance.bubbleSort(nums.copy())
    endTime = time.time()
    print("Bubble sort takes time(s):", round(endTime - startTime, 5))
    # Select sort
    startTime = time.time()
    sortMachineInstance.selectSort(nums.copy())
    endTime = time.time()
    print("Select sort takes time(s):", round(endTime - startTime, 5))
    # Insert sort
    startTime = time.time()
    sortMachineInstance.insertSort(nums.copy())
    endTime = time.time()
    print("Insert sort takes time(s):", round(endTime - startTime, 5))
    # Quick sort
    startTime = time.time()
    sortMachineInstance.quickSort(nums.copy())
    endTime = time.time()
    print("Quick sort takes time(s):", round(endTime - startTime, 5))
    # Merge sort
    startTime = time.time()
    sortMachineInstance.mergeSort(nums.copy())
    endTime = time.time()
    print("Merge sort takes time(s):", round(endTime - startTime, 5))