ikyu_scraper
====

Downloader and scraper of ikyu.com for NLP research.
This is a fork from a project by Toshihiko Yanase.
(https://bitbucket.org/toshihikoyanase/ikyu_scraper)

言語処理研究のためのikyu.comのダウンローダ＆スクレイパー。

2017/10/31時点で動作確認済みです。

## Requirement

* Python 2.7
* pip

## Install

```
pip install -r requirements.txt
```

## Usage

### 全アクション実行

```
make
```

### Step-by-step 解説

地域の一覧ページ（`トップ > ホテル・旅館一覧`）から地域のURLリストを抽出する。

```
mkdir -p build
python get_last_link_list.py https://www.ikyu.com/ap/srch/UspW15001.aspx | \
    tee build/ikyu-area.txt
```


各地域のホテル一覧ページからホテルのURLリストを抽出する
- ikyu.comのホテルのクチコミのページネーションの最後のページを表示
- そのURLをテキストファイルurl_list.txtに1行1件で記録

```
python download_hotel_urls.py build/ikyu-area.txt | tee build/url_list.txt
```

HTMLファイルのダウンロードする

```
python dl.py build/url_list.txt build/html_dir
```

HTMLファイルからテキストとレーティングをスクレイプする

```
bash scrape_all.sh build/html_dir build/json_dir
```


## License

LICENSEに記したように、本コードのライセンスはCC0です。

These codes are licensed under CC0 as shown in LICENSE.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)