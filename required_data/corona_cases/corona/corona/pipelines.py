# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter


class CoronaPipeline:
    def __init__(self):
        """
        Init method
        """
        self.conn = None
        self.cursor = None
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("corona_cases.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""drop table if exists country_wide_data""")
        self.cursor.execute("""drop table if exists world_wide_data""")
        self.cursor.execute("""create table country_wide_data(
            country text,
            cases text,
            deaths text,
            new_cases text,
            new_deaths text,
            active_cases text,
            recovered_cases text
        )""")

        self.cursor.execute("""create table world_wide_data(
            total_cases text,
            total_deaths text,
            total_recovered text,
            total_active_cases text,
            total_active_normal text,
            total_active_serious text,
            total_closed text
        )""")

    def process_item(self, item, spider):
        self.store_data(item)

        # print("pipeline: country", item['country_wide_data'][0])
        # print("pipeline: world  ", item['world_wide_data']['total_active_cases'])
        return item

    def store_data(self, item):
        for i in range(len(item['countries'])):
            self.cursor.execute("""insert into country_wide_data values (?,?,?,?,?,?,?)""",(
                item['countries'][i],
                item['cases'][i],
                item['deaths'][i],
                item['new_cases'][i],
                item['new_deaths'][i],
                item['active_cases'][i],
                item['recovered'][i]
            ))

        self.cursor.execute("""insert into world_wide_data values (?,?,?,?,?,?,?)""",(
            item['total_cases'],
            item['total_deaths'],
            item['total_recovered'],
            item['total_active_cases'],
            item['total_active_normal'],
            item['total_active_serious'],
            item['total_closed']
        ))

        self.conn.commit()
