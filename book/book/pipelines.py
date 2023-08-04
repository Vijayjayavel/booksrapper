# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookPipeline:

    def __int__(self):

        self.create_conncection()
        self.create_table()


    def create_conncection(self):
        self.conn=sqlite3.connect('books.db')
        self.cur=self.conn.cursor()

    def create_table(self):
        self.cur.execute("""drop table if exists book""")
        self.cur.execute("""create table book(name varchar(255),price varchar(50),photo varchar(255))""")
    def process_item(self, item, spider):
        self.store_db(item)
        print('pipeline: '+item['name'][0])
        return item
    def store_db(self,item):
        self.cur.execute("""insert into books values(?,?,?)""",
                          (item['name'],item['price'],item['photo']))
        self.conn.commit()
        return item
