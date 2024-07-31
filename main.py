import requests
from bs4 import BeautifulSoup as bs
import json

def main():

    url_genre_file = {
        "https://www.webtoons.com/en/genres/drama?sortOrder=READ_COUNT":"drama.json",
        "https://www.webtoons.com/en/genres/fantasy?sortOrder=READ_COUNT":"fantasy.json",
        "https://www.webtoons.com/en/genres/comedy?sortOrder=READ_COUNT":"comedy.json",
        "https://www.webtoons.com/en/genres/action?sortOrder=READ_COUNT":"action.json",
        "https://www.webtoons.com/en/genres/slice_of_life?sortOrder=READ_COUNT":"slice of life.json",
        "https://www.webtoons.com/en/genres/romance?sortOrder=READ_COUNT":"romance.json",
        'https://www.webtoons.com/en/genres/super_hero?sortOrder=READ_COUNT':"superhero.json",
        "https://www.webtoons.com/en/genres/sf?sortOrder=READ_COUNT":"sci-fi.json",
        "https://www.webtoons.com/en/genres/thriller?sortOrder=READ_COUNT":'thriller.json',
        "https://www.webtoons.com/en/genres/supernatural?sortOrder=READ_COUNT":"supernatural",
        "https://www.webtoons.com/en/genres/mystery?sortOrder=READ_COUNT":"mystery.json",
        "https://www.webtoons.com/en/genres/sports?sortOrder=READ_COUNT":"sports",
        "https://www.webtoons.com/en/genres/historical?sortOrder=READ_COUNT":"historical.json",
        "https://www.webtoons.com/en/genres/heartwarming?sortOrder=READ_COUNT":"heartwarming.json",
        "https://www.webtoons.com/en/genres/horror?sortOrder=READ_COUNT":"horror.json",
        "https://www.webtoons.com/en/genres/tiptoon?sortOrder=READ_COUNT":"informative.json"

        }
    
    for url, genre_list in url_genre_file.items():


        page = requests.get(url)
        soup = bs(page.text, "html.parser")

        all_manwha = soup.find("ul", class_="card_lst")

        manwha_info_list = []

        for item in all_manwha.find_all("li"):
            title = item.find("p", class_="subj").get_text()
            author = item.find("p", class_="author").get_text()
            likes = item.find('em', class_='grade_num').get_text()

            manwha_info_list.append({"Title": title, "Author": author, "Likes": likes})
        

        #json file
        with open(genre_list, 'w') as json_file:
            json.dump(manwha_info_list, json_file, indent=5)

        #check data
        for manwha in manwha_info_list:
            print(f"\tTITLE: {manwha['Title']}\n\tAUTHOR: {manwha['Author']}\n\tLIKES: {manwha['Likes']}\n")


if __name__ == "__main__":
    main()


