import psycopg2
while True:
    
    try:
        conn = psycopg2.connect(host="localhost", database="test", user="gitpod", password="Mohamed")

        curs = conn.cursor()

        print("Succrss")
        break

    except Exception as e:
        print("Error : ", format(e))


