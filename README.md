# test-lp-pages

このレポジトリは、Github Pages で公開するためのサンプルランディングページを含んでいます。

## 使い方

1. このレポジトリをクローンします。
2. `index.html` を編集します。
3. 変更をコミットしてプッシュします。
4. GitHub Pages 上でページが更新されます。

## 公開URL

https://wararaki718.github.io/test-lp-pages/

## Github Pages + Actions の設定方法

Settings -> Pages -> Source で Github Actions を選択します。
これで、Github Actions 側のデプロイ（`.github/workflows/deploy.yml`）が有効になり、`main` ブランチへのプッシュ時に自動的に GitHub Pages が更新されるようになります。

## 運用比較早見表

| 方式                   | 概要                        | 運用のしやすさ | 自由度 |   自動化 |
| -------------------- | ------------------------- | ------: | --: | ----: |
| ① HTMLを直接配置          | HTMLを作ってGitHub Pagesで公開   |       △ |   ◎ |     △ |
| ② LPごとのHTML + 一覧自動生成 | HTMLは直接作るが、一覧だけActionsで生成 |       ○ |   ◎ |     ○ |
| ③ YAML → HTML自動生成    | YAMLだけ編集し、HTMLはActionsで生成 |   **◎** |   ○ | **◎** |
