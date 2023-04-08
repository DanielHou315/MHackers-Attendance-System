import requests
import pyshorteners
from datetime import datetime
'''

There are a few things this script does: 

1. Create a google form and a google sheet
2. Aggregate the google form 

Planned Future Support 
1. Custom Naming Scheme for form and url link
'''

SHORT_URL = "NULL"
LONG_URL = "NULL"





def print_obvious(content):
    print()
    print(content)
    print()


def tiny_url(original_url, api_key):
    dateobj = datetime.today()
    aliasing = "mhackers{0}{1}{2}".format(dateobj.year, dateobj.month, dateobj.day)

    headers = {"Content-Type": "application/json"}
    check_params = {"api_token": api_key}
    update_params = {     
        "api_token": api_key,  
        "url": original_url,
        "domain": 'tinyurl.com',
        "alias": aliasing
    }

    # Check if existing
    ch_existing = requests.get(f'https://api.tinyurl.com/alias/tinyurl.com/{aliasing}', params=check_params)
    
    # If existing, update the code  
    if ch_existing.status_code == 200:
        update_rtn = requests.patch('https://api.tinyurl.com/change/', headers=headers, params=update_params)
        if update_rtn.status_code == 200:
            print_obvious(f"Changed URL: https://tinyurl.com/{aliasing}")
            return f"https://tinyurl.com/{aliasing}"
        else:
            raise Exception("Error Changing URL: ", update_rtn.json()['errors'])
    else:
        new_rtn = requests.post('https://api.tinyurl.com/create/', headers=headers, params=update_params)
        if new_rtn.status_code == 200:
            print_obvious(f"New URL: https://tinyurl.com/{aliasing}")
            return f"https://tinyurl.com/{aliasing}"
        else:
            raise Exception("Error Creating URL: ", new_rtn.json()['errors'])


def main():
    # shorten_url("https://www.danielhou.me/", "vOjwsUIxEZOcpVfXBh7WF3lwnvWeminEYVKw0cpVc7e5DBerdu2nzCZk5O7Y")
    tiny_url("https://www.drive.google.com/", "vOjwsUIxEZOcpVfXBh7WF3lwnvWeminEYVKw0cpVc7e5DBerdu2nzCZk5O7Y")
    return


if __name__ == "__main__":
    main()
    


