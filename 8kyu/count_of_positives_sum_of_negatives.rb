# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
#
# If the input array is empty or null, return an empty array:
#
# C#/Java: new int[] {} / new int[0];
# C++: std::vector<int>();
# JavaScript/CoffeeScript/TypeScript/PHP/Haskell: [];
# Rust: Vec::<i32>::new();
# ATTENTION!
# The passed array should NOT be changed. Read more here.
#
# For example:
#
# input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# return [10, -65].

def count_positives_sum_negatives(lst)
  positive_count = lst.map { |x| x if x > 0 }.compact
  negative_sum = lst.map { |x| x if x < 0 }.compact
  negative_sum = negative_sum.inject(0){|sum, num| (num < 0) ? sum + num : sum}
  result = [positive_count.count]
  p result.push(negative_sum)
end

count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
#  10,-65])
