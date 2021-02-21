import psycopg2
#connect to the db 
con = psycopg2.connect(
            host = "localhost",
            database="mydb",
            user = "postgres",
            password = "postgres")

#cursor 
cur = con.cursor()
#cur.execute("insert into mydbtable (id,marks) values (%s, %s)", (4, "90") )
#execute query
cur.execute("select * from test3")
rows = cur.fetchall()

for r in rows:
    print (f"id {r[0]} name {r[1]}")

#commit the transcation 
#con.commit()

#close the cursor
cur.close()

#close the connection
con.close()