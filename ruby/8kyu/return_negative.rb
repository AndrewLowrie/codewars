# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# makeNegative(1); # return -1
# makeNegative(-5); # return -5
# makeNegative(0); # return 0

def makeNegative(num)
  if num > 0
    return num * -1
  elseif num == 0
    return 0
  else num < 0
    return num
  end
end
