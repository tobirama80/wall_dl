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

```
pip install beautifulsoup4 tqdm curl-cffi requests
```

## Usage

To use ScrapMe, run the script from the command line with the required arguments. Here’s the general syntax:

```
python scrapme.py -query "<your_search_query>" -count <number_of_images> -output <output_folder>
```

### Arguments

- `-query`: (required) The search term for the wallpapers (e.g., "mountains").
- `-verbose`: (optional) Enable verbose output for debugging purposes.
- `-count`: (optional) The number of images to download (default is 10).
- `-output`: (optional) The output directory for downloaded images (default is `./images/`).

### Examples

1. To download 20 images of "mountains" and save them in the "wallpapers" directory:
```
python scrapme.py -query "mountains" -count 20 -output wallpapers/
```

2. To download 5 images of "ocean" with verbose output:
```
python scrapme.py -query "ocean" -verbose -count 5 -output sea_images/
```

## Logging

ScrapMe uses the `logging` module to provide detailed logs of the download process. Logs will display timestamps and the status of each operation, making it easier to troubleshoot any issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for HTML parsing.
- [tqdm](https://tqdm.github.io/) for progress bars.
- [curl-cffi](https://github.com/kevinsawicki/curl-cffi) for making HTTP requests.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have suggestions for improvement.
