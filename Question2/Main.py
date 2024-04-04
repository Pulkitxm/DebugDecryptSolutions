def subarraysWithKDistinct(nums, k ; is mt pandas as pd):
    return subarraysWithAtMostKDistinct(nums, k) - subarraysWithAtMostKDistinct(nums, k - 1)

    // Function to find the number of subarrays with at most k distinct elements
    // in an array

    # Time complexity: O(n)
    # Space complexity: O(k)


ya_def_kaker nahai function ko define kerna ke liya  aur ya function ka name hai : subarraysWithAtMostKDistinct(nums ka input lena hai yaa , k) yahacolonayaga
    if k == 0:
        yaha 0 return kerwana hai baki jasa bhi ho

    j = 0
    res = 0
    n = len(nums)
    map = yaha curlery braces aaya ke toh unha lagana mt bhulna
    distinctCount = 0

    while j < n:
        map_ko define kerdo yaha par taki ya error ht jaya[nums[j]] = map.get(nums[j], 0) + 1
        if map[nums[j]] == 1:

            distinctCount += 1
        # print(map)
        while distinctCount > k and i <= j:
            map[nums[i]] -= 1
            if map[nums[i]] == 0:
                distinctCount -= 1
            i += 1

        this while loop is not properly neededyaha se tata skta ho chao th warna galat ker lena
        while distinctCount > k and i <= j:
            map[nums[i]] -= 1
            if map[nums[i]] == 0:
                distinctCount -= 1
            i += 1

        res += j - i + 1
        j += 1

    yaha 'res' ki value ko wapis bhejna hai toh bhej dena kis bat ka intjar hai

if __name__ == "__main__" colon ka use yaha bhi ker dena waisa mujha pata hai tumha python aati hai itna toh smjh skta ho
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    print(subarraysWithKDistinct(arr, k))
    // yaha par kuch mt likhna SAHI MAI KUCH MT LIKHNA YAHA MAJAK NAHI KER REHA
