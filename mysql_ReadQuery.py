from mysql.connector import connect
from sshtunnel import SSHTunnelForwarder
sql_hostname = '127.0.0.1'
sql_username = 'ugrp'
sql_password = 'ugrp'
sql_main_database = 'UGRP'
sql_port = 3306
ssh_host = '13.209.76.22'
ssh_user = 'ubuntu'
ssh_password = 'ugrp'
ssh_port = 22
with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_password=ssh_password,
        remote_bind_address=(sql_hostname, sql_port)) as tunnel:
    connection = connect(
        user=sql_username,
        password=sql_password,
        host=sql_hostname,
        database=sql_main_database,
        port=sql_port,
        auth_plugin='mysql_native_password'
    )
