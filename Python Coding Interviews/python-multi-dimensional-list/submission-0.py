from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    maxes = []
    for i in range(len(nested_arr)):
        temp = 0
        for j in range(len(nested_arr[i])):
            if nested_arr[i][j] > temp:
                temp = nested_arr[i][j]
        maxes.append(temp)
    return maxes


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
