# Word2Vec API Server

Simple API Server for Word2Vec based on Tornado

![python](https://img.shields.io/badge/python-3.6.5-green.svg)
![tornado](https://img.shields.io/badge/tornado-5.1.1-blue.svg)
![gensim](https://img.shields.io/badge/gensim-3.6.0-blue.svg)

## Usage

1. Clone this repo

    ```bash
    $ git clone https://github.com/tashirovii/word2vec-api-server
    ```

2. Download pre-trained word2vec model from below link and Move to `media/models/`

    [Pre-trained word vectors of 30+ languages](https://github.com/Kyubyong/wordvectors)

3. Run API Server

    ```bash
    $ docker-compose up -d
    ```

4. Send request and get response

    ```
    https://xxx.xxx.xxx.xxx:8888/similar?words=日本,ソニー
    ```

    ```javascript
    {
      "日本": {
          "ドイツ": 0.5213180780410767,
          "インドネシア": 0.45377278327941895,
          "トカラ": 0.4508639872074127,
          "京外": 0.4432913661003113,
          "ヨーロッパ": 0.43235597014427185,
          "イギリス": 0.4233030676841736,
          "タイ": 0.42056766152381897,
          "スワヒリ": 0.4189295768737793,
          "ロシア": 0.41537922620773315,
          "アジア": 0.41487473249435425
      },
      "ソニー": {
          "キヤノン": 0.7392974495887756,
          "パナソニック": 0.7136946320533752,
          "アップル": 0.7097973823547363,
          "ソニーミュージックエンタテインメント": 0.7032612562179565,
          "アップルコンピュータ": 0.6995246410369873,
          "マイクロソフト": 0.6883590221405029,
          "モトローラ": 0.6840162873268127,
          "ケンウッド": 0.6832154989242554,
          "ノキア": 0.6695355176925659,
          "テイチク": 0.6672531366348267
      }
    }
    ```
