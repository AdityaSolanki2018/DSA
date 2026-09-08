def twoSum(numbers: list, target: int) -> list:
        my_map = {}
        for i in range(len(numbers)):
            required =  target - numbers[i]
            if required in my_map:
                return [my_map[required]+1,i+1]
            else:
                my_map[numbers[i]] = i

