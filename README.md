# About
The whole purpose of this project is to understand how we can move data from OLTP database to OLAP database and check performance of data read apis in both databases. Data Flow on OLTP Database is through GraphQL queries. 

## How to Create Celery Beat Task

The idea here is we will run cron job on regular interval which will check for new entries in database and push these new entries to **RabbitMQ** queue.  We will run celery workers in which will consume these messages from queue.

We are here using **django celery beat** for task schedule. It use django database for task management. 

To create celery beat cron job follow below steps

 - Create celery task and then run django server.
 - Go to admin interface of Django
 - Go to Periodic task 
 - Create a new task and make sure celery beat is running
 - For this database migration job please provide `[taskname, model_name, exchange_name, queue_name, routing_key]` in arguments.
 - You can use celery flower to monitor workers.

