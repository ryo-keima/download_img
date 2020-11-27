import os
import urllib.error
import urllib.request
import ssl

# 例 googleのロゴ
url = 'https://pbs.twimg.com/profile_images/874463635950551040/IhlhyWsq_400x400.jpg'
# カレントディレクトリ
path = os.getcwd()

def down_load_img(url, path):
    ''' URLを指定し、画像を指定のフォルダに配置する '''
    # ファイル名の作成
    values = url.split('/')
    filename = values[-1]
    filename = filename.split('.')[0]
    # ファイルパスの指定
    if os.name == 'posix':
        path = '{}/{}.jpg'.format(path, filename)
    elif os.name == 'nt':
        path = '{}\\{}.jpg'.format(path, filename)
    
    print(path)

    # 画像URLからダウンロード
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

down_load_img(url, path)
