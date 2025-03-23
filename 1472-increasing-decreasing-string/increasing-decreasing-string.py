from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        counter_dict = Counter(s)
        sort_arr = sorted(set(s))
        result  = ''

        while counter_dict:
            for string in sort_arr:
                if counter_dict[string] > 0:
                    result += string
 
                    counter_dict[string] -= 1

                else:
                    if string in counter_dict:
                        counter_dict.pop(string)


            for string in sort_arr[::-1]:
                if counter_dict[string] > 0:
                    result += string
                    counter_dict[string] -= 1
                else:
                    if string in counter_dict:
                        counter_dict.pop(string)
        return result
