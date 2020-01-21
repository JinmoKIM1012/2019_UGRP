from mysql.connector import connect
from sshtunnel import SSHTunnelForwarder
import pprint


def mysqlDpt():
    sql_hostname = '127.0.0.1'
    sql_username = 'ugrp22'
    sql_password = 'ugrp'
    sql_main_database = 'UGRP'
    sql_port = 3306
    ssh_host = '13.209.76.22'
    ssh_user = 'ubuntu'
    ssh_password = 'ugrp'
    ssh_port = 22
    try:
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
                port=tunnel.local_bind_port,
                auth_plugin='mysql_native_password'
            )
            try:
                cursor = connection.cursor()
                query = ("show Columns from dptPostech")
                cursor.execute(query)
                data = cursor.fetchall()

                query = ("select dptName, dptCallNum, dptFax, dptLoc, dptExp, dptGradNum from dptPostech")
                cursor.execute(query)
                data = cursor.fetchall()

                dptLst = [i[0] for i in data]
                connection.commit()

                cursor.close()
                connection.close()
                return data
            except:
                return None
            finally:
                cursor.close()
                connection.close()
    except:
        return None


if __name__ == '__main__':
    data_res = mysqlDpt()
    pprint.pprint(data_res)
