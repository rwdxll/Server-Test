## 查询每天注册人数、发布商品、创建订单
```
SELECT
	DATE_FORMAT(T1.createTime,"%Y-%m-%d") as CreateTime,
	Total_User as 每天注册用户,
	Total_Goods as 每天发布商品,
	Total_Orders as 每天创建订单
FROM (
	(
		SELECT
			date_format(createTime, "%Y-%m-%d") AS createTime,
			count(*) AS Total_User
		FROM
			t_user
		GROUP BY
			date_Format(createTime, "%Y-%m-%d") desc
	)t1,
	(
		SELECT
			date_format(createTime, "%Y-%m-%d") AS createTime,
			count(*) AS Total_Goods
		FROM
			t_goods_auditing
		GROUP BY
			date_Format(createTime, "%Y-%m-%d") desc
	) t2,
	(
		SELECT
			date_format(createTime, "%Y-%m-%d") AS createTime,
			count(*) AS Total_Orders
		FROM
			t_orders
		GROUP BY
			date_Format(createTime, "%Y-%m-%d") desc
	) t3 )
where t1.createTime=t2.createTime and t2.createTime=t3.createTime

```
## 按照价格区间统计
```
select price_range,count(id) as 成功交易的笔数,sum(price) as 订单总金额 from (
SELECT
	id,
	(orderMoney+postage) AS price,
	CASE
	when (orderMoney+postage) <= 10 THEN "<=10"
	when 10 < (orderMoney+postage) and (orderMoney+postage) <=100 then ">10且≤100"
	when 100 < (orderMoney+postage) and (orderMoney+postage) <=500 then ">100且≤500"
	when 500 < (orderMoney+postage) and (orderMoney+postage) <=1000 then ">500且≤1000"
	when 1000 < (orderMoney+postage) and (orderMoney+postage) <=3000 then ">1000且≤3000"
	when 3000 < (orderMoney+postage) and (orderMoney+postage) <=5000 then ">3000且≤5000"
	when 5000 < (orderMoney+postage) and (orderMoney+postage) <=8000 then ">5000且≤8000"
	when 8000 < (orderMoney+postage) and (orderMoney+postage) <=10000 then ">8000且≤10000"
	when 10000 < (orderMoney+postage) and (orderMoney+postage) <=15000 then ">10000且≤15000"
	when 15000 < (orderMoney+postage) and (orderMoney+postage) <=20000 then ">15000且≤20000"
	when 20000 < (orderMoney+postage) then ">20000"
	end as price_range
FROM
	t_orders
WHERE
	orderStatus != "close")t1
group by price_range
```
## mysql之累加
```
SET @x = 0;
SELECT
	t1.months,
	t1.register_num ,
	@x := @x + t1.register_num AS total_register
FROM
	(
		SELECT
			DATE_FORMAT(createTime, "%Y%m") months,
			count(id) AS register_num
		FROM
			t_user
		GROUP BY
			months asc
	) t1
```
