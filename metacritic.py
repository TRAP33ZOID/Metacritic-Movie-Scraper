import requests
from bs4 import BeautifulSoup

def scrape_metacritic_must_see_movies():
    base_url = "https://www.metacritic.com"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Header to mimic a browser visit

    must_see_movies = []

    # Loop through the first two pages
    for page_num in range(1, 3):
        url = f"{base_url}/browse/movie/all/mystery/all-time/userscore/?genre=mystery&releaseYearMin=1910&releaseYearMax=2023&page={page_num}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            movie_containers = soup.find_all('a', class_="c-finderProductCard_container g-color-gray80 u-grid")

            for container in movie_containers:
                if container.find('img', class_="c-finderProductCard_mustImage"):
                    # Extract the movie name from the href attribute
                    movie_name = container.get('href').split('/')[2]
                    must_see_movies.append(movie_name.replace('-', ' ').title())
        else:
            print(f"Failed to retrieve page {page_num}")

    return must_see_movies

# Run the function and print the results
movies = scrape_metacritic_must_see_movies()
print("Must-See Movies:", movies)
