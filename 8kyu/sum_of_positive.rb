# You get an array of numbers, return the sum of all of the positives ones.
#
# Example [1,-4,7,12] => 1 + 7 + 12 = 20

def positive_sum(arr)
  t = 0
  p = 0
  while (p<arr.length) do
    if arr[p] > 0
      t += arr[p]
    end
    p += 1
  end
  return t
end
