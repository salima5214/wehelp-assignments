# README

# 要求二：建立資料庫和資料表

    透過任何方式，
    連結到 MySQL 伺服器中進行管理，完成以下動作：
    1. 建立一個新的資料庫，取名字為 website。
    2. 在資料庫中，建立會員資料表，取名字為 member。

![](https://i.imgur.com/V4wyOXP.png)

![](https://i.imgur.com/oP55AWr.png)

![](https://i.imgur.com/kA4hRnk.png)

![](https://i.imgur.com/MYEBgn7.png)

![](https://i.imgur.com/CZO6r8a.png)

![](https://i.imgur.com/42izZ5e.png)

# 要求三：SQL CRUD

    利用要求二建立的資料庫和資料表，寫出能夠滿足以下要求的 SQL 指令：
    參考教學文件：W3Schools SQL Tutorial
    ● 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
    ● 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
    ● 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
    ● 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
    ● 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
    ● 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
    ● 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

![](https://i.imgur.com/DgZZjbp.png)

![](https://i.imgur.com/CicEqOT.png)

![](https://i.imgur.com/cCHVUGy.png)

![](https://i.imgur.com/v3oguZN.png)

![](https://i.imgur.com/oUvvk5i.png)

![](https://i.imgur.com/Rn2H5To.png)

![](https://i.imgur.com/ML67IX1.png)

## 要求四：SQL Aggregate Functions

    利用要求二建立的資料庫和資料表，寫出能夠滿足以下要求的 SQL 指令：
    ● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
    ● 取得 member 資料表中，所有會員 follower_count 欄位的總和。
    ● 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

![](https://i.imgur.com/dHteeHL.png)

![](https://i.imgur.com/jwAbQQY.png)

![](https://i.imgur.com/jtCXXw8.png)

## 要求五：SQL JOIN (Optional)

    在資料庫中，建立新資料表，取名字為 message。
    ● 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
    ● 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有
    留言，資料中須包含留言者會員的姓名。


![](https://i.imgur.com/ZA0v276.png)

![](https://i.imgur.com/kiRFIpl.png)

![](https://i.imgur.com/1QlJu4t.png)

![](https://i.imgur.com/ndoODUO.png)

![](https://i.imgur.com/VIB8FiM.png)

![](https://i.imgur.com/dflSnSO.png)

