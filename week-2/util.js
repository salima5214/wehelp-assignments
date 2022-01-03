// ###################### 要求一：函式與流程控制 ######################

function calculate(min, max)
{
    // 請用你的程式補完這個函式的區塊
    var sum = 0;
    var value = min;

    while(true)
    {
        if (value > max)
        {
            break;
        }
    
        sum   += value;
        value += 1;
    }
    console.log(sum);
}
calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30

// ######################## 要求二：典與列表 #########################

function avg(data)
{
    // 請用你的程式補完這個函式的區塊
    var total_salary = 0

    for(var index = 0; index < data["count"]; index++){
        total_salary += data["employees"][index][ 'salary'];
    }

    average_salary = total_salary / data["count"]
    console.log(average_salary)
}


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
}); // 呼叫 avg 函式

// #################### 要求三：演算法 [maxProduct] ##################

function maxProduct(nums)
{
    // 請用你的程式補完這個函式的區塊
    var temp_max_product = -Infinity;
    for(var i = 0; i < nums.length-1; i++)
    {
        for(var j = i+1; j < nums.length; j++)
        {
            if (nums[i] * nums[j] > temp_max_product)
            {
                temp_max_product = nums[i] * nums[j];
            }
        }
    }
    console.log(temp_max_product)
}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0

// ####################### 要求四：演算法 [twoSum] ###################

function twoSum(nums, target)
{
    // your code here
    for(var i = 0; i < nums.length-1; i++)
    {
        for(var j = i+1; j < nums.length; j++)
        {
            if (nums[i] + nums[j] == target)
            {
                return [i, j];
            }
        }
    }
}

let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

// ##################### 要求四：演算法 [maxZeros] ###################

function maxZeros(nums)
{
    var temp_max_zeros = 0
    var current_zeros = 0
    var flag = true
    // 請用你的程式補完這個函式的區塊
    for(var i = 0; i < nums.length; i++)
    {
        if(nums[i] == 0 && flag)
        {
            flag = false;
            current_zeros = 1;
        }
        else if(nums[i] == 0 && !flag)
        {
            current_zeros += 1;
            if(i == nums.length-1)
            {
                if(current_zeros > temp_max_zeros)
                {
                    temp_max_zeros = current_zeros;
                }
            }                
        }
        else if(nums[i] == 1 && !flag)
        {
            flag = true;
            if(current_zeros > temp_max_zeros){
                temp_max_zeros = current_zeros;
            }
        } 
    }
    console.log(temp_max_zeros);
}

maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]) // 得到 3