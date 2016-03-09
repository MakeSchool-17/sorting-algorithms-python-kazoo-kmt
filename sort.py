import time
import unittest

def timed_sort(list, key, algorithm='insertion'):
    sort_func = globals()[algorithm]
    start_time   = time.time()
    sorted_list  = sort_func(list, key=key)
    end_time     = time.time()
    elapsed_time = end_time - start_time
    return (sorted_list, elapsed_time)

# ---
# Define your search algorithm functions here!

def insertion(list, key=lambda item: item):
    size = len(list)
    for i in range(1, size):
        for j in range(i, 0, -1):
            compare = list[j - 1]
            current = list[j]
            if key(current) < key(compare):
                list[j] = compare
                list[j - 1] = current

return list


def bucket(list):
    """assuming it contains [0, 10]"""
    result = []
    # list comprehension: [] for X in X
    buckets = [[] for number in range(0, 11)]
    
    # assign list items to each bucket
    for number in list:
        buckets[number].append(number)

    for bucket in buckets:
        # for number in bucket:
        #     result.append(number)
        
        # result += bucket  #this is worst because it includes copy and assign
        result.extend(bucket)

return result

# You can also implement by dictionary (we've done in histogram)


class TestSorting(unittest.TestCase):
    def test_bucket_sort(self):
        list = [1, 5, 4, 7, 6, 8, 4, 2, 9, 1, 5, 4, 6, 8]
        expected_result = sorted(list)
        bucket_sorted = bucket(list)
        self.assertEqual(bucket_sorted, expected_result)
        print('original list:', list)
        print('sorted list:', bucket_sorted)
# print(expected_result == bucket_sorted)


if __name__ == '__main__':
    unittest.main()
