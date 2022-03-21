# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# import mysql.connector
from itemadapter import ItemAdapter
# import sqlite3
# import _mysql_connector
#
# class PresentMirrorPipeline:
#
#     def __init__(self):
#         self.create_connections()
#         self.create_tables()
#
#     def create_connections(self):
#         # self.conn = sqlite3.connect("mydatabase.db")
#         self.conn = mysql.connector.connect(
#             host = 'localhost',
#             user = 'root',
#             password = 'root',
#             database = 'mysql_pm'
#         )
#         self.curr = self.conn.cursor()
#
#     def create_tables(self):
#         self.curr.execute("""DROP TABLE IF EXISTS present_mirror""")
#         self.curr.execute("""create table present_mirror(title text, author text, tag text)""")
#
#     def process_item(self, item, spider):
#         self.store_db(item)
#         # print("pipeline :" + item['title'][0])
#         return item
#
#     def store_db(self, item):
#         # self.curr.execute("""INSERT INTO present_mirror VALUES(?,?,?)""",(
#         #                   item['title'][0],
#         #                   item['author'][0],
#         #                   item['tag'][0]
#         #                   ))
#
#         self.curr.execute("""INSERT INTO present_mirror VALUES(%s,%s,%s)""",(
#             item['title'][0],
#             item['author'][0],
#             item['tag'][0]
#         ))
#         self.conn.commit()
