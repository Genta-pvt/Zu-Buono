# Zu-Buono
## 概要
**リンク：[Zu-buono!](https://develop.drj8uetlwdud8.amplifyapp.com/ )**  
"ずぼーの" = ずぼらでBuono(イタリア語でおいしい)なレシピを投稿 & 閲覧するwebアプリケーションです。  
一般のレシピ投稿サイトと違うのは、投稿できる情報が極めて制限されていることです。  
例えば材料は5種類まで、作り方は200文字までしか投稿できません。  
これにより、投稿されるレシピは作るのに手間がかからず、作りやすいレシピに限られます。
## 機能の説明
- ### レシピ投稿機能  
    レシピの内容をwebページのフォームに記入して、投稿できます。
    - **料理画像投稿機能 (実装予定)**  
    レシピを投稿するとき、料理の画像も投稿できます.
- ### レシピ閲覧機能  
    投稿されたレシピの一覧からレシピを選んで情報を閲覧できます。
## AWS構成  
![AWS Architect](https://i.imgur.com/DP0krph.jpg)  
### CI/CD開発環境を構築しています  
GitHubとAmplify、AWS Lambdaを紐づけしているので、GitHubでマージすることで、自動的に最新版がデプロイされます。  
今後、共同開発者が増えた場合でも、スムーズに開発を進行できます。
## 使用技術  
### バックエンド(Lambda)  
- Python
    - バージョン
        > Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32  
### フロントエンド  
- HTML
    - バージョン
        > HTML5  
- JavaScript
### AWS基盤
- Amplify
- AWS Lambda
- API Gateway
- DynamoDB
- IAM
### 自動デプロイ  
- GitHub Action
- Amplify

## 開発環境  
- Pycharm  
  - バージョン
    > PyCharm 2022.3.1 (Community Edition)

- git
    - バージョン
        > git version 2.39.0.windows.1  
## OS
- Windows
    - バージョン  
        > エディション	Windows 10 Home  
        > バージョン	21H2  
        > インストール日	2021/01/15  
        > OS ビルド	19044.2251  