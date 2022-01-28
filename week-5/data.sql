# 建立一個新的資料庫，取名字為 website。
CREATE DATABASE `website`; # SHOW DATABASES; # DROP DATABASE `website`;
USE `website`;

# 在資料庫中，建立會員資料表，取名字為 member。
CREATE TABLE `member`(
	`id` BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT COMMENT '獨立編號',
    `name` VARCHAR(255) NOT NULL COMMENT '姓名',
    `username` VARCHAR(255) NOT NULL COMMENT '帳號名稱',
    `password` VARCHAR(255) NOT NULL COMMENT '帳戶密碼',
    `follower_count` INT NOT NULL DEFAULT '0' COMMENT '追蹤者數量',
    `time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '註冊時間'
);

DESCRIBE `member`; # DROP TABLE `member`;

# 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
INSERT INTO `member` VALUES(1, 'TEST', 'test', 'test', 10, now()+10), (2, 'SALIMA', 'salima', '666', 20, now()+9), (3, 'LUCY', 'lucy', '777', 30, now()+8), (4, 'JOY', 'joy', '888', 40, now()+7), (5, 'SOS', 'sos', '999', 50, now()+6);

# 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
SELECT * FROM `member`;

# 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
SELECT * 
FROM `member`
ORDER BY `time` DESC; # ASC

# 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
SELECT * 
FROM `member`
ORDER BY `time` DESC
LIMIT 1, 3;

# 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
SELECT * 
FROM `member`
WHERE `username` = 'test'; # 不等於 <>

# 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
SELECT * 
FROM `member`
WHERE `username` = 'test' AND `password` = 'test';

# 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
SET SQL_SAFE_UPDATES = 0;
UPDATE `member`
SET `name` = 'test2'
WHERE `username` = 'test';

#  取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
SELECT COUNT(*) FROM `member`;

# 取得 member 資料表中，所有會員 follower_count 欄位的總和。
SELECT SUM(`follower_count`) FROM `member`;

# 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
SELECT AVG(`follower_count`) FROM `member`;

############################################################
# 在資料庫中，建立新資料表，取名字為 message。

# DROP TABLE `message`;
CREATE TABLE `message`(
	`id` BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT COMMENT '獨立編號',
    `member_id` BIGINT NOT NULL COMMENT '留言者會員編號',
    `content` VARCHAR(255) NOT NULL COMMENT '留言內容',
    `time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '留言時間',
     FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
);

INSERT INTO `message` VALUES(11, 5, "I like it!", now()+2), (22, 1, "hahaha", now()+4), (33, 3, "XDDD", now()+6), (44, 1, "nice~~", now()+8), (55, 2, "wow...", now()+10), (66, 2, "good~", now()+12), (77, 1, "> <", now()+14);

DESCRIBE `message`;
SELECT * FROM `message`;

# 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
SELECT *
FROM `message`
INNER JOIN `member`
ON `message`.`member_id` = `member`.`id`;

# 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
SELECT *
FROM `message`
INNER JOIN `member`
ON `message`.`member_id` = `member`.`id`
WHERE `username` = 'test';