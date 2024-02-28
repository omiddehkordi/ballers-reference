import scrapy
import string
from nbascraper.PerGameSeason import PerGameSeason

class BbalRefSpider(scrapy.Spider):
    name = "nba_rookies"
    allowed_domains = ["basketball-reference.com"]
    start_urls = ["https://basketball-reference.com"]

    def start_requests(self):
        last_name_initials = list(string.ascii_lowercase)
        print(last_name_initials)
        base_player_url = "https://www.basketball-reference.com/players/"
        urls = [base_player_url + x + '/' for x in last_name_initials]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        base_url = 'https://www.basketball-reference.com'

        for active_player in response.xpath('//div[@id="div_players"]/table[@id="players"]/tbody/tr'):
            start_year = active_player.xpath('td[@data-stat="year_min"]/text()').get()
            player_name = active_player.xpath('th/strong/a')

            if start_year == '2024' and player_name:
                url = base_url + player_name.xpath('@href').get()
                yield scrapy.Request(url=url, callback=self.parse_player_page)

    def parse_player_page(self, response):
        name = response.xpath('//div[@id="info" and @class="players"]//div/h1/span/text()').get()
        #experience = response.xpath('//div[@id="info" and @class="players"]//div[2]/p[11]/text()').get()

        for season in response.xpath('//div[@id="div_per_game"]/table[@id="per_game"]/tbody/tr[@class="full_table"]'):
            player = PerGameSeason()

            player["name"] = name

                # Need to loop through each season (each season is organized as a row)
                # foreach season in seasons ('//tbody/tr[@class="full_table"]')
            player["season"] = season.xpath('th[@data-stat="season"]/a/text()').get()
            player["age"] = season.xpath('td[@data-stat="age"]/text()').get()
            player["team"] = season.xpath('td[@data-stat="team_id"]/a/text()').get()
            player["league"] = season.xpath('td[@data-stat="lg_id"]/a/text()').get()
            player["position"] = season.xpath('td[@data-stat="pos"]/text()').get()
            player["games_played"] = season.xpath('td[@data-stat="g"]/text()').get()
            player["games_started"] = season.xpath('td[@data-stat="gs"]/text()').get()
            player["minutes_played_per_game"] = season.xpath('td[@data-stat="mp_per_g"]/text()').get()
            player["field_goals_per_game"] = season.xpath('td[@data-stat="fg_per_g"]/text()').get()
            player["field_goals_attempted_per_game"] = season.xpath('td[@data-stat="fga_per_g"]/text()').get()
            player["field_goal_percentage"] = season.xpath('td[@data-stat="fg_pct"]/text()').get()
            #player["experience"] = experience

            player["blocks_per_game"] = season.xpath('td[@data-stat="blk_per_g"]/text()').get()
            player["turnovers_per_game"] = season.xpath('td[@data-stat="tov_per_g"]/text()').get()
            player["personal_fouls_per_game"] = season.xpath('td[@data-stat="pf_per_g"]/text()').get()
            player["points_per_game"] = season.xpath('td[@data-stat="pts_per_g"]/text()').get()

        yield player
