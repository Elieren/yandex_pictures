import requests
from bs4 import BeautifulSoup
import os
import platform
import re


class UrlImage():

    def __init__(self, search, value=30, iw=None, ih=None):
        self.__search = search
        self.__value = value
        self.__iw = iw
        self.__ih = ih

    def parse(self):
        j = 0
        i = 0
        status = True
        self.__image_link = []
        self.__image_link2 = []

        while status:
            url = f'https://yandex.ru/images/search?from=tabbar \
                &text={self.__search}&p={i}&isize=eq \
                    &iw={self.__iw}&ih={self.__ih}'

            responce = requests.get(url).text
            soup = BeautifulSoup(responce, 'lxml')
            block = soup.find(
                "div",
                class_='serp-controller__content'
            )
            all_image = block.find_all("div", class_='serp-item__preview')

            for image in all_image:
                if j < self.__value:
                    self.__image_link.append(image.find('a').get('href'))
                    self.__image_link2.append(image.find(
                        'img',
                        class_='serp-item__thumb justifier__thumb'
                    ).get('src'))
                    j += 1
                else:
                    status = False
                    break
            i += 1

        return self.__image_link, self.__image_link2


class Download():

    def __init__(self, image_link, image_link2, value, level, direct):
        self.__image_link = image_link
        self.__image_link2 = image_link2
        self.__value = value
        self.__os_platform = platform.system().lower()
        self.__level = level
        self.__direct = direct

        try:
            self.__image_normal_save_select()

        except requests.exceptions.ConnectionError:
            self.__error_url()

    def __image_normal_save_select(self):

        url_image = re.split('img_url=|&from', self.__image_link)

        normal_link = url_image[1].replace('%3A', ':').replace(r'%2F', '/') \
            .replace('%25', '%').replace('%28', '(').replace('%29', ')')

        image_bytes = requests.get(normal_link).content

        with open(f'{self.__direct}/{self.__value}.jpg', 'wb') as file:
            file.write(image_bytes)

        if self.__level == 0:
            if self.__os_platform == 'windows':
                os.system(f"{self.__direct}\\{self.__value}.jpg")
            else:
                os.system(f"{self.__direct}/{self.__value}.jpg")

            while True:
                select = input("save (YES/NO): ")

                select = select.lower()

                if select == 'yes':
                    break

                elif select == 'no':
                    os.remove(f"{self.__direct}/{self.__value}.jpg")
                    break

                else:
                    pass
        else:
            print("Picture", self.__value)

    def __error_url(self):

        url = f'http:{self.__image_link2}'

        image_bytes = requests.get(url).content

        with open(f'{self.__direct}/{self.__value}.jpg', 'wb') as file:
            file.write(image_bytes)

        if self.__level == 0:
            if self.__os_platform == 'windows':
                os.system(f"{self.__direct}\\{self.__value}.jpg")
            else:
                os.system(f"{self.__direct}/{self.__value}.jpg")

            while True:
                select = input("save (YES/NO): ")

                select = select.lower()

                if select == 'yes':
                    break

                elif select == 'no':
                    break
                    os.remove(f"{self.__direct}/{self.__value}.jpg")

                else:
                    pass

        else:
            print("Picture", self.__value)

# =============================================================================


search = input('search: ')

value = int(input('How many pictures to parse: '))

image_link, image_link2 = UrlImage(search, value).parse()

select = input("Download all pictures or select one. (All/No): ").lower()

direct = input('Directory where to save: ')

for value in range(len(image_link)):

    if select == 'no':
        Download(image_link[value], image_link2[value], value, 0, direct)

    elif select == 'all':
        Download(image_link[value], image_link2[value], value, 1, direct)

    else:
        pass
