import requests
import sys
from tools import valid_string

endpoint = 'https://api.github.com/users/{username}/events'

def main():
    user = input('User: ').strip()
    if valid_string(user):
        print('Invalid user. Try again.')
        sys.exit(1)
    
    activities = requests.get(endpoint.format(username = user)).json()
    for activity in activities:
        match activity['type']:
            case 'PushEvent':
                commits = len(activity['payload']['commits'])
                print(f'Pushed {commits} {"commit" if commits == 1 else "commits"} to {activity['repo']['name']}')
            case 'IssuesEvent':
                print(f'Opened a new issue in {activity['repo']['name']}')
            case 'WatchEvent':
                print(f'Starred {activity['repo']['name']}')

if __name__ == '__main__':
    main()