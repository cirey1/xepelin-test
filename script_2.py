def find_and_multiply(nums, expected_sum=2022):
    for pos1 in range(0, len(nums)):
        for pos2 in range(pos1 + 1, len(nums)):
            if nums[pos1] + nums[pos2] == expected_sum:
                return nums[pos1] * nums[pos2]
    return False


if __name__ == "__main__":
    result = find_and_multiply(nums=[20, 2034, 1000, 1022])
    print(result)
