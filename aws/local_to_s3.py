import boto3

def upload_file_to_s3(local_file_path, bucket_name, destination_path):
    s3_client = boto3.client('s3')
    
    s3_client.upload_file(local_file_path, bucket_name, destination_path)

# Example usage:
local_file_path = '/Users/omid/Desktop/ROY_Project/web_scrapers/nbascraper/nbascraper/spiders/nba_rookies.csv'
bucket_name = 'nba-rookie-project'
destination_path = 'rookie_stats/nba_rookies.csv'

upload_file_to_s3(local_file_path, bucket_name, destination_path)