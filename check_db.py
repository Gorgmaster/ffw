import sqlite3


def checkTime():
    
    conn = sqlite3.connect('/home/amweb/zeitsteuerung.db')
    cursor = conn.cursor()
    
    sql = '''SELECT *
            FROM zeitsteuerung
            WHERE DATETIME('now', 'localtime') BETWEEN an AND aus;'''
            
    cursor.execute(sql)
    
    rows = cursor.fetchall()
    
    if len(rows) > 0:
        return True
    else:
        return False
    



if __name__ == '__main__':
    
    ret = checkTime()
    print(ret)
    