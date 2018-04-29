# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(str)
  str = str.split('')
  counter = 0
  result = []
  while counter < str.length
    if str[counter+1] == nil
      result = result.push(str[counter] + "_")
    else
      result = result.push(str[counter] + str[counter+1])
    end
    counter += 2
  end
  return result
end
