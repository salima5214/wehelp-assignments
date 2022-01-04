##################################################################
###################### 要求一：函式與流程控制 ######################
##################################################################

def calculate(min, max):
    # 請用你的程式補完這個函式的區塊
    sum = 0
    value = min

    while True:
        if value > max:
            break

        sum   += value
        value += 1

    print(sum)


calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

##################################################################
######################## 要求二：典與列表 #########################
##################################################################

def avg(data):
    # 請用你的程式補完這個函式的區塊
    total_salary = 0

    for index in range(data["count"]):
        total_salary += data["employees"][index]["salary"]

    average_salary = total_salary / data["count"]
    print(average_salary)


avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
}) # 呼叫 avg 函式

##################################################################
#################### 要求三：演算法 [maxProduct] ##################
##################################################################

def maxProduct(nums):
    temp_max_product = - float("inf")
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] * nums[j] > temp_max_product:
                temp_max_product = nums[i] * nums[j]
    print(temp_max_product)

# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2


##################################################################
####################### 要求四：演算法 [twoSum] ###################
##################################################################

def twoSum(nums, target):
    # your code here
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

##################################################################
##################### 要求四：演算法 [maxZeros] ###################
##################################################################

def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    temp_max_zeros = 0
    current_zeros = 0
    flag = True

    for i in range(len(nums)):
        if nums[i] == 0 and flag:
            flag = False
            current_zeros = 1
        elif nums[i] == 0 and not flag:
            current_zeros +=1 
            if i == len(nums)-1 :
                if current_zeros > temp_max_zeros:
                    temp_max_zeros = current_zeros
        elif nums[i] == 1 and not flag:
            flag = True
            if current_zeros > temp_max_zeros:
                temp_max_zeros = current_zeros
    
    print(temp_max_zeros)        

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3