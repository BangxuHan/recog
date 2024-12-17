import requests
import base64
import json
import argparse
import os
IMAGES_FORMAT = ['.jpg', '.JPG', '.png']  # 图片格式


def search_test(commit_image, url):
    with open(commit_image, "rb") as f:
        data = f.read()
        bstr = base64.b64encode(data)
        bstr = str(bstr, encoding="utf-8")
        da = {"image": [bstr, bstr]}
        res = requests.post(url=url, json=da)
        if res.ok:
            print(commit_image)
            result = json.loads(res.text)
            print(result)
            print("ok")
        else:
            result = None

        return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="查询参数")
    parser.add_argument('-url', type=str, default='http://127.0.0.1:5000/charrecog')
    parser.add_argument('-image_path', type=str, default='test1')

    args = parser.parse_args()
    url = args.url
    image_path = args.image_path

    image_names = [name for name in os.listdir(image_path) for item in IMAGES_FORMAT if
                   os.path.splitext(name)[1] == item]
    image_names.sort()
    n_len = len(image_names)

    if n_len > 0:
        for w in range(n_len):
            commit_image_path = os.path.join(image_path, image_names[w])
            # for i in range(1000):
            result = search_test(commit_image_path, url)

