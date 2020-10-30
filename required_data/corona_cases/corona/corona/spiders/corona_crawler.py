import scrapy
from ..items import CoronaItem


class CoronaCases(scrapy.Spider):
    """
    This class is used to get the details / data from the web.

    """
    name = 'corona'
    start_urls = [
        "https://virusncov.com"
    ]

    def parse(self, response):
        items = CoronaItem()

        items['total_cases'] = response.css(".first-count span").css("::text").get()
        items['total_deaths'] = response.css(".mt-large .red-text").css("::text").get()
        items['total_recovered'] = response.css(".mt-large .green-text").css("::text").get()
        items['total_active_cases'] = response.css(".col-50:nth-child(1) .firt-div span:nth-child(1)").css(
            "::text").get()
        items['total_active_normal'] = response.css(".pupp-text").css("::text").get()
        items['total_active_serious'] = response.css(".second-div .red-text").css("::text").get()
        items['total_closed'] = response.css(".col-50+ .col-50 .firt-div span:nth-child(1)").css("::text").get()

        items['countries'] = [country for country in response.css("td:nth-child(2)").css("::text").extract() if
                              country.split()]
        items['cases'] = response.css("td:nth-child(3)").css("::text").extract()
        items['deaths'] = [death.css("::text").get() if death.css("::text").extract() else 0 for death in
                           response.css("td:nth-child(5)")]
        items['new_cases'] = [case.css("::text").get().split()[0].replace('+', '') if case.css("::text").get() else 0
                              for case in response.css("td:nth-child(4)")]
        items['new_deaths'] = [death.css("::text").get().split()[0].replace('+', '') if death.css("::text").get() else 0
                               for death in response.css("td:nth-child(6)")]
        items['active_cases'] = [case.css("::text").get() if case.css("::text").get() else '0' for case in
                                 response.css("td:nth-child(7)")]
        items['recovered'] = [case.css("::text").get() if case.css("::text").get() else '0' for case in
                              response.css("td:nth-child(8)")]

        yield items


class CoronaCases2(scrapy.Spider):
    """
    This class is used to get the details / data from the web.

    """
    name = 'corona2'
    start_urls = [
        "https://www.worldometers.info/coronavirus/"
    ]

    def parse(self, response):
        cases = response.css(".sorting_1").css("::text").extract()
        total = response.css("#maincounter-wrap:nth-child(7) span").css("::text").extract()

        # yield cases
        yield {
            "total_cases_2": total,
            "country_cases": cases,
        }
