import psycopg2

users = 'postgres'
dbnames='postgres'
passwords='postgres'
conn= psycopg2.connect(" user=" + users +" dbname=" + dbnames +" password=" + passwords)

cur = conn.cursor()

select_sql = 'SELECT lon,lat FROM test;'
for row in cur.execute(select_sql):
    print(row)
