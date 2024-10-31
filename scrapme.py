import argparse
import logging
from tqdm import tqdm
from bs4 import BeautifulSoup
from curl_cffi import requests
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='scrapme - %(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class Downloader:
    def __init__(self, query, count, output):
        self.query = query
        self.count = count
        self.path = os.path.join(output, query.replace(" ", "_"))
        self.links = []
        self.src_links = []
        os.makedirs(self.path, exist_ok=True)  # Create output directory if it doesn't exist

    def start_download(self):
        for i in tqdm(range(len(self.src_links)), desc="Downloading images"):
            try:

                response = requests.get(self.src_links[i], stream=True, impersonate='chrome')
                filename = self.src_links[i].split('/')[-1]
                with open(os.path.join(self.path,filename), 'wb') as f:
                    for chunk in response.iter_content():
                        if chunk:
                            f.write(chunk)
            except Exception as e:
                logging.error(f"Failed to download {self.links[i]}: {e}")

    def get_links(self):
        query = self.query.replace(" ", "+")
        response = requests.get(f"https://www.wallpaperflare.com/search?wallpaper={query}", impersonate='chrome')
        with open('page.html', 'w',encoding='utf-8',errors='ignore') as f:
            f.write(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', itemprop='url')

        for index, item in enumerate(links):
            if index >= self.count:
                break
            link = item['href']
    
            if link:
                # Extract the src from the <img> tag
                self.links.append(link)
    def get_src_links(self):
        for i in self.links:
            resp = requests.get(i)
            soup = BeautifulSoup(resp.text, 'html.parser')
            thumbnail_link = soup.find('link', itemprop='thumbnail')
            # Extract the href attribute if the tag exists
            if thumbnail_link:
                href = thumbnail_link['href']
                self.src_links.append(href)
    def main(self):
        self.get_links()
        if self.links:
            logging.info(f"Found {len(self.links)} images for the query: {self.query}")
            self.get_src_links()
            self.start_download()
        else:
            logging.warning("No images found for the given query.")

def main():
    parser = argparse.ArgumentParser(
        description='A tool for downloading wallpaper from the "wallpaperflare.com" website.',
        epilog='Examples:\n'
               'Usage: scrapme.py -query "mountains" -verbose -count 20 -output wallpapers/\n'
               'Usage: scrapme.py -query "ocean" -count 5 -output sea_images/',
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Adding flag arguments
    parser.add_argument('-query', type=str, required=True, help='Search Query')
    parser.add_argument('-verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('-count', type=int, default=10, help='Number of Images')
    parser.add_argument('-output', type=str, default='./images/', help='Output folder name')

    args = parser.parse_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    downloader = Downloader(args.query, args.count, args.output)
    downloader.main()

if __name__ == '__main__':
    main()
