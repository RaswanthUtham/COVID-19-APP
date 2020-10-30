import re
import os
import sqlite3
import pyttsx3
import subprocess
import speech_recognition as sr
from scrapy.crawler import CrawlerProcess
from required_data.corona_cases.corona.corona.spiders.corona_crawler import CoronaCases


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception:", str(e))
    return said.lower()


def update_via_cmd():
    path_ = os.getcwd()
    os.chdir(r"..\required_data\corona_cases\corona")
    subprocess.check_output(['scrapy', 'crawl', 'corona'])
    os.chdir(path_)
    return None


def update_data():
    process = CrawlerProcess()
    process.crawl(CoronaCases)
    process.start()


class Data:
    def __init__(self):
        """
        Init method
        """
        self.conn = None
        self.cursor = None
        self._create_connection()
        self.world_wide_data = {}
        self.country_wide_data = {}

    def _create_connection(self):
        self.conn = sqlite3.connect(r"..\required_data\corona_cases\corona\corona_cases.db")
        self.cursor = self.conn.cursor()

    def _get_world_wide_cases(self):
        data = self.cursor.execute("select * from world_wide_data")
        x = data.fetchone()
        self.world_wide_data = {"cases": x[0], "deaths": x[1], "recovered": x[2], "active cases": x[3],
                                "normal": x[4], "critical": x[5], "closed": x[6]}

    def _get_country_wide_cases(self):
        data = self.cursor.execute("select * from country_wide_data")
        self.country_wide_data = {country.lower(): {"cases": case,
                                                    "deaths": death,
                                                    "new cases": nc,
                                                    "new deaths": nd,
                                                    "active cases": ac,
                                                    "recovered cases": rc,
                                                    } for country, case, death, nc, nd, ac, rc in data
                                  }

    def get_data(self):
        self._get_world_wide_cases()
        self._get_country_wide_cases()
        self.conn.close()
        return self.world_wide_data, self.country_wide_data


def main():
    print("Started Program")
    data = Data()
    world_wide_data, country_wide_data = data.get_data()
    country_list = [country for country in country_wide_data.keys()]
    print(world_wide_data)
    print(country_wide_data)

    # patterns
    new = re.compile(r".*new.*")
    case = re.compile(r".*case.*")
    death = re.compile(r".*death.*")
    active = re.compile(r".*active.*")
    recover = re.compile(r".*recover.*")
    normal = re.compile(r".*normal.*|.*health.*")
    critical = re.compile(r".*critical.*|.*serious.*")
    closed = re.compile(r".*close.*")

    while True:
        print("Listening...")
        text = speech_to_text()
        print(text)
        result = None
        country = None

        words = set(text.split(" "))
        for word in words:
            if word in country_list:
                country = word

        if new.match(text) and death.match(text):
            if country:
                result = country_wide_data.get(country).get("new deaths")
            else:
                result = world_wide_data.get("deaths")

        elif new.match(text) and case.match(text):
            if country:
                result = country_wide_data.get(country).get("new cases")
            else:
                result = world_wide_data.get("cases")

        elif active.match(text):
            if country:
                result = country_wide_data.get(country).get("active cases")
            else:
                result = world_wide_data.get("active cases")

        elif recover.match(text):
            if country:
                result = country_wide_data.get(country).get("recovered cases")
            else:
                result = world_wide_data.get("recovered")

        elif critical.match(text):
            result = world_wide_data.get("critical")

        elif normal.match(text):
            result = world_wide_data.get("normal")

        elif closed.match(text):
            result = world_wide_data.get("closed")

        elif case.match(text):
            if country:
                result = country_wide_data.get(country).get("cases")
            else:
                result = world_wide_data.get("cases")

        elif death.match(text):
            if country:
                result = country_wide_data.get(country).get("deaths")
            else:
                result = world_wide_data.get("deaths")

        if result:
            text_to_speech(result)

        if text.find('stop') != -1:  # stop loop
            print("Exit")
            break


if __name__ == "__main__":
    update_via_cmd()
    text_to_speech("Hi I am Corona Bot, what do you want mother fucker thai-yo-lee!!!")
    main()
