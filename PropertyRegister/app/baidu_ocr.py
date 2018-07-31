# -*- coding: utf-8 -*-
import json
from aip import AipOcr

APP_ID = '11608090'
API_KEY = 'ZVoA0aeuSi3P0iWK9DbBXYUY'
SECRET_KEY = 'OYUUKqTIsnxr7p5pbcRTOgqYtuYn50nR '
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
base_path = 'C:/Users/marsy/OneDrive/Documents/BitBucket/PropertyRegiester/PropertyRegister/app/static/uploads/'


def _get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


def baidu_ocr(image_file):
    image_path_file = base_path + image_file
    image = _get_file_content(image_path_file)
    """ API options """
    options = {"language_type": "CHN_ENG",
               "detect_direction": "true",
               "detect_language": "true",
               "probability": "true"}
    res = client.basicGeneral(image, options)
    data = res['words_result']
    # print(type(res))
    # data = json.load(res)
    ls = []
    for k in data:
        ls.append(k['words'])
    return ls


# def main():
#     baidu_ocr('1.jpg')
#
#
# if __name__ == '__main__':
#     main()