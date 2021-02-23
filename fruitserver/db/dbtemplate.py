from cx_Oracle import connect, Connection, Cursor


class DbTemplate:
    def __init__(self, user="fruit", pwd="123456", dns="localhost/xe", encoding="UTF-8"):
        self.__conn = connect(user, pwd, dns, encoding=encoding)

    def save_update(self, sql, **keyargs):
        count = -1
        cur = None
        try:
            # 获取游标对象
            cur = self.__conn.cursor()

            # 执行SQL语句
            cur.execute(sql, keyargs)

            # 获取语句影响的记录数
            count = cur.rowcount

            # 事务提交（写入数据库）
            self.__conn.commit()
        except Exception as ex:
            # 事务回滚（撤消写入数据）
            self.__conn.rollback()

            # 抛出异常
            raise ex
        finally:
            if cur:
                cur.close()
        return count

    def close(self):
        self.__conn.close()

    def find(self, sql, **keyargs):
        data = []

        with self.__conn.cursor() as cur:
            cur.execute(sql, keyargs)
            # data = cur.fetchall()
            for record in cur:
                item = {}
                for i in range(len(cur.description)):
                    key = cur.description[i][0]
                    item[key]=record[i]
                    # print(item)
                data.append(item)
        return data





if __name__ == "__main__":
    dbtmp = DbTemplate("fruit", "123456", "localhost/xe")
    # sql = "insert into admin values(seq_admin.nextval, :name,:pwd,:status)"
    # dbtmp.save_update(sql, name="Li", pwd="333444", status=0)

    data = dbtmp.find("select * from admin where admin_name=:name and pwd=:pwd and status=:status", name="Jack", pwd="123456", status=1)
    print(data)

    dbtmp.close()