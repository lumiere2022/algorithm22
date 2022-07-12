def solution(nums):
    set_nums = set(nums)
    len_set, len_mon = len(set_nums), len(nums)//2
    if len_set <= len_mon:
        return len_set
    return len_mon
