1 - run makemigrations and migrate 
    $ python manage.py makemigrations
    $ python manage.py migrate

2 - seed the database (there is a fixture for base app)
    # The data model based on - https://www.w3schools.com/sql/sql_join.asp
    $ python manage.py loaddata base_data.json.gz

3 - create a view table in databse using pgAdmin (for postgres), in your case
    use navicat.

    CREATE VIEW order_list AS
        SELECT base_customers.id, base_customers.customer_name, base_orders.order_date
        FROM base_orders
        INNER JOIN base_customers ON base_orders.customer_id=base_customers.id

4 - Open shell 
    $ python manage.py shell
    >> from base.database_view import OrderList
    >> OrderList.objects.all().values()

More info check out the screenshots
