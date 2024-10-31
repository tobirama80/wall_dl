# ScrapMe: Wallpaper Downloader

ScrapMe is a Python tool designed to download wallpapers from the website [wallpaperflare.com](https://www.wallpaperflare.com). It allows users to search for specific wallpaper queries and download a specified number of images directly to their local machine.

## Features

- Search for wallpapers using a query string.
- Download a specified number of images.
- Save images in an organized directory structure.
- Verbose logging to track the download process.

## Requirements

- Python 3.x
- `beautifulsoup4`
- `tqdm`
- `curl-cffi`
- `requests` (if using instead of curl_cffi)

You can install the required libraries using pip:

```bash
pip install beautifulsoup4 tqdm curl-cffi requests
```
## Usage
To use ScrapMe, run the script from the command line with the required arguments. Here’s the general syntax:
```bash
python scrapme.py -query "<your_search_query>" -count <number_of_images> -output <output_folder>
```
