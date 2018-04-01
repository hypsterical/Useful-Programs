# Quick number picking program for raffles. Based on the current entires (curr_nums),
# will choose the number you should select that has the highest odds of winning
# Rules are assumed to be "closest number wins"

curr_nums = [2501, 45, 3037, 1005, 4999, 1192, 1193, 4089, 420, 3456, 3337, 2732, 4863, 82, 808, 696, 742, 401, 4200, 3113, 4632, 2121, 0, 3535, 1569, 2104, 892, 1717, 3000, 1995, 4000, 1926, 3579, 3867, 1988, 520, 3666, 5000, 1999, 602, 1738, 1825, 1138, 718, 2525, 1206, 888, 322, 2441, 3682, 1869, 14, 1212, 1777, 3113, 303, 2222, 219, 1492, 3574, 671, 2, 1998, 1056, 587, 2969, 377, 1029, 1408, 4343, 4479, 3982, 1337, 3567, 2016, 7, 4321, 111, 359, 2340, 14, 322, 4118, 215, 2017, 3745, 99, 1080, 639, 3789, 1988, 42, 1719, 2998, 3717, 1717]
min_num = 0
max_num = 5000
print (curr_nums)
curr_best = 0
num_to_pick = -1
curr_low = -1
curr_high = -1
curr_nums.append(min_num)
curr_nums.append(max_num)
curr_nums.sort()
print ("Sorted numbers chosen so far:")
print (curr_nums)
for i in range(0, len(curr_nums) - 1):
    curr_low = curr_nums[i]
    curr_high = curr_nums[i+1]
    if (curr_high - curr_low) > curr_best:
        num_to_pick = curr_low + (curr_high - curr_low) / 2
        curr_best = curr_high - curr_low

odds = curr_best / (max_num - min_num)
print("By picking the number " + str(num_to_pick) + " you are covering a spread of " +  str(curr_best) + " numbers and have an odds of winning of " + str(odds))
        