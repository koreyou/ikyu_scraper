ikyu_scraper
====

Downloader and scraper of ikyu.com for NLP research.

言語処理研究のためのikyu.comのダウンローダ＆スクレイパー。

FIXME: ページネーションのURLが変わっているため、このままでは動きません。

## Requirement

* Python 2.7
* pip

## Usage

URLのリストを作る
- ikyu.comのホテルのクチコミのページネーションの最後のページを表示
- そのURLをテキストファイルurl_list.txtに1行1件で記録

HTMLファイルのダウンロードする

```
bash dl.py url_list.txt html_dir
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