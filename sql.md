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
