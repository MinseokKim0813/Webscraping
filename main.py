import requests
from bs4 import BeautifulSoup

def scrape(url):
    # TODO
    print(url)
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to scrape. Code: {response.status_code}")
            return -1
        # Problem here
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except Exception as e:
        print(f"Error: {e}")

def main():
    url = "https://www.beehive.ae/"
    result = scrape(url)
    print(result)

if __name__ == "__main__":
    main()