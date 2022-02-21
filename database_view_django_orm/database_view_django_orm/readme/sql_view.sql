CREATE VIEW order_list AS
	SELECT base_customers.id, base_customers.customer_name, base_orders.order_date
	FROM base_orders
	INNER JOIN base_customers ON base_orders.customer_id=base_customers.id
