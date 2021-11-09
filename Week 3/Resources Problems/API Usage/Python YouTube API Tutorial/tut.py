from googleapiclient.discovery import build

api_key = ''

youtube = build('youtube', 'v3', developerKey = api_key)

request = youtube.channels().list(part = 'statistics', id = 'UCDogdKl7t7NHzQ95aEwkdMw')

response = request.execute()

print(response)