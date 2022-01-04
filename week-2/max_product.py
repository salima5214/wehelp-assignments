

def maxProduct(nums):
    temp = []
    zero_flag = False
    for i in range(len(nums)):  
        if nums[i] == 0:
            zero_flag = True
            continue
        else:
            temp.append(nums[i])

    positive_count = 0
    negative_count = 0

    first_max = - float("inf")
    second_max = - float("inf")
    first_min =  float("inf")
    second_min =  float("inf")

    for i in range(len(temp)):
        if temp[i] > 0:
            positive_count += 1
            if temp[i] > first_max:
                second_max = first_max
                first_max = temp[i]
            elif temp[i] > second_max:
                second_max = temp[i]
        else:
            negative_count += 1
            if temp[i] < first_min:
                second_min = first_min
                first_min = temp[i]
            elif temp[i] < second_min:
                second_min = temp[i]

    if positive_count > 1 and negative_count > 1:
        if first_max*second_max > first_min*second_min:
            print(first_max*second_max) 
        else:
            print(first_min*second_min) 
    elif positive_count > 1:
            print(first_max*second_max) 
    elif negative_count > 1:
            print(first_min*second_min) 
    elif zero_flag:
        print(0)
    else:
        print(temp[0]*temp[1])


# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

