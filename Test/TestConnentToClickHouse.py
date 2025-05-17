from clickhouse_driver import Client
client = Client(
    host = 'cc-bp1ly584pa39j1v62.public.clickhouse.ads.aliyuncs.com',
    port = '3306',
    user = 'admin',
    password = 'FDDabc021202',
    database = 'testtab_test01'
)

try:
    result = client.execute('SELECT * FROM test_tbl_local')
    print("result:",result)
except Exception as e:
    print("连接失败:",e)