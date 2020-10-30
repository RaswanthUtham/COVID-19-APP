# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoronaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    total_cases = scrapy.Field()
    total_deaths = scrapy.Field()
    total_recovered = scrapy.Field()
    total_active_cases = scrapy.Field()
    total_active_normal = scrapy.Field()
    total_active_serious = scrapy.Field()
    total_closed = scrapy.Field()

    countries =scrapy.Field()
    cases = scrapy.Field()
    deaths =  scrapy.Field()
    new_cases =scrapy.Field()
    new_deaths = scrapy.Field()
    active_cases = scrapy.Field()
    recovered = scrapy.Field()

    # world_wide_data = {
    #         "world wide cases": total_cases,
    #         "world wide deaths": total_deaths,
    #         "world wide recovered": total_recovered,
    #         "world wide active cases": total_active_cases,
    #         "world wide closed cases": total_closed,
    #         "world wide active but not serious": total_active_normal,
    #         "world wide active and serious": total_active_serious,
    #     }
    # for country, i in enumerate(countries):
    #     country_wide_data = {
    #         "Country": country,
    #         "nof_cases": cases[i], 
    #         "nof_deaths": deaths[i], 
    #         "nof_new_cases": new_cases[i], 
    #         "nof_new_deaths": new_deaths[i], 
    #         "active": active_cases[i], 
    #         "recovered": recovered[i],
    #     }

    
