# Python MySQL CRUD Example

Steps:

1. Install Python.

2. Install dependencies.

```
pip3 install flask_table
pip3 install pymysql
pip3 install flask-mysql
```

3. Create MySQL DB roytuts and run the following query:

```
CREATE TABLE `tbl_user` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_email` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_password` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
```

4. Follow the tutorial avoiding the similar steps above: https://www.roytuts.com/python-web-application-crud-example-using-flask-and-mysql/

5. Run the code to start the server:
```
python main.py
```

6. Access the URL on the browser:
```
http://localhost:5000/
```
