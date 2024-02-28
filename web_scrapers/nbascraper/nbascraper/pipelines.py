# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class NbascraperPipeline:
    def open_spider(self, spider):
        self.file = open('nba_rookies.csv', 'w', newline='')
        self.writer = csv.DictWriter(self.file, fieldnames=['name', 'season', 'age', 'team', 'league', 'position', 'games_played', 'games_started', 'minutes_played_per_game', 'field_goals_per_game', 'field_goals_attempted_per_game', 'field_goal_percentage', 'blocks_per_game', 'turnovers_per_game', 'personal_fouls_per_game', 'points_per_game'])  # Add all required fieldnames here
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow({
            'name': item.get('name'),
            'season': item.get('season'),
            'age': item.get('age'),
            'team': item.get('team'),
            'league': item.get('league'),
            'position': item.get('position'),
            'games_played': item.get('games_played'),
            'games_started': item.get('games_started'),
            'minutes_played_per_game': item.get('minutes_played_per_game'),
            'field_goals_per_game': item.get('field_goals_per_game'),
            'field_goals_attempted_per_game': item.get('field_goals_attempted_per_game'),
            'field_goal_percentage': item.get('field_goal_percentage'),
            'blocks_per_game': item.get('blocks_per_game'),
            'turnovers_per_game': item.get('turnovers_per_game'),
            'personal_fouls_per_game': item.get('personal_fouls_per_game'),
            'points_per_game': item.get('points_per_game')
        })
        return item

    def close_spider(self, spider):
        self.file.close()
