ikyu_scraper
====

Downloader and scraper of ikyu.com for NLP research.
This is a fork from a project by Toshihiko Yanase.
(https://bitbucket.org/toshihikoyanase/ikyu_scraper)

言語処理研究のためのikyu.comのダウンローダ＆スクレイパー。

FIXME: ページネーションのURLが変わっているため、このままでは動きません。

## Requirement

* Python 2.7
* pip

## Usage

地域の一覧ページ（`トップ > ホテル・旅館一覧`）から地域のURLリストを抽出する。

```
python get_last_link_list.py https://www.ikyu.com/ap/srch/UspW15001.aspx | \
    tee etc/ikyu-area.txt
```


各地域のホテル一覧ページからホテルのURLリストを抽出する
- ikyu.comのホテルのクチコミのページネーションの最後のページを表示
- そのURLをテキストファイルurl_list.txtに1行1件で記録

```
python download_hotel_urls.py etc/ikyu-area.txt | tee url_list.txt
```

HTMLファイルのダウンロードする

```
python dl.py url_list.txt html_dir
```

HTMLファイルからテキストとレーティングをスクレイプする

```
bash scrape_all.sh html_dir json_dir
```

## Install


```
pip install -r requirements.txt
```


## License

LICENSEに記したように、本コードのライセンスはCC0です。

These codes are licensed under CC0 as shown in LICENSE.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)