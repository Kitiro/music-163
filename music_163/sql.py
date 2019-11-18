"""
一般 Python 用于连接 MySQL 的工具：pymysql
"""
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='wyy',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def create_tabels():
    tabels = ['artists', 'albums', 'comments', 'musics']
    tabels_info = ['ARTIST_ID varchar(10) primary key, ARTIST_NAME varchar(10)',
            'ALBUM_ID varchar(15) primary key, ARTIST_ID varchar(10)',
            'MUSIC_ID varchar(20), COMMENTS varchar(100), DETAILS varchar(100)',
            'MUSIC_ID varchar(20), MUSIC_NAME varchar(20), ALBUM_ID varchar(15)']
    with connection.cursor() as cursor:
        sql = "CREATE TABLE  {} ({});"
        for i,j in zip(tabels, tabels_info):
            exe = sql.format(i,j)
            print(exe)
            cursor.execute(exe)
    connection.commit()

# 保存评论
def insert_comments(music_id, comments, detail, connection0):
    with connection0.cursor() as cursor:
        sql = "INSERT INTO `comments` (`MUSIC_ID`, `COMMENTS`, `DETAILS`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (music_id, comments, detail))
    connection0.commit()


# 保存音乐
def insert_music(music_id, music_name, album_id):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `musics` (`MUSIC_ID`, `MUSIC_NAME`, `ALBUM_ID`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (music_id, music_name, album_id))
    connection.commit()


# 保存专辑
def insert_album(album_id, artist_id):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `albums` (`ALBUM_ID`, `ARTIST_ID`) VALUES (%s, %s)"
        cursor.execute(sql, (album_id, artist_id))
    connection.commit()


# 保存歌手
def insert_artist(artist_id, artist_name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `artists` (`ARTIST_ID`, `ARTIST_NAME`) VALUES (%s, %s)"
        cursor.execute(sql, (artist_id, artist_name))
    connection.commit()


# 获取所有歌手的 ID
def get_all_artist():
    with connection.cursor() as cursor:
        sql = "SELECT `ARTIST_ID` FROM `artists` ORDER BY ARTIST_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取所有专辑的 ID
def get_all_album():
    with connection.cursor() as cursor:
        sql = "SELECT `ALBUM_ID` FROM `albums` ORDER BY ALBUM_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取所有音乐的 ID
def get_all_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取前一半音乐的 ID
def get_before_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID LIMIT 0, 800000"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取后一半音乐的 ID
def get_after_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID LIMIT 800000, 1197429"
        cursor.execute(sql, ())
        return cursor.fetchall()


def dis_connect():
    connection.close()

if __name__ == "__main__":
    create_tabels()
