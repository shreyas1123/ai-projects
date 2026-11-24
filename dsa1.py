def has_duplicates(nums):
    seen =set()
    for x in nums:
        if x in seen:
            return True
        else:
            seen.add(x)
    return False
x=print(has_duplicates([1,3,5,3,5]))
