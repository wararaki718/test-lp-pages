from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader


CONTENT_DIR = Path("content")
TEMPLATE_DIR = Path("templates")
OUTPUT_DIR = Path("pages")


def main():
    # Jinja2の設定
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR)
    )

    template = env.get_template("lp.html")

    # 出力先を作成
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    lp_names = []

    # content/*/page.yaml を処理
    for lp_dir in sorted(CONTENT_DIR.iterdir()):

        if not lp_dir.is_dir():
            continue

        yaml_file = lp_dir / "page.yaml"

        if not yaml_file.exists():
            continue

        # LP名を記録
        lp_names.append(lp_dir.name)

        # YAMLを読み込む
        with yaml_file.open(encoding="utf-8") as f:
            data = yaml.safe_load(f)

        # 出力ディレクトリ
        output_dir = OUTPUT_DIR / lp_dir.name
        output_dir.mkdir(parents=True, exist_ok=True)

        # HTMLを生成
        html = template.render(**data)

        # HTMLを書き出す
        output_file = output_dir / "index.html"

        output_file.write_text(
            html,
            encoding="utf-8"
        )

        print(f"Generated: {output_file}")

    # --------------------------------
    # LP一覧ページを生成
    # --------------------------------

    links = []

    for lp_name in lp_names:
        links.append(
            f'<li><a href="./{lp_name}/">{lp_name}</a></li>'
        )

    index_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LP一覧</title>
</head>

<body>

<h1>LP一覧</h1>

<ul>
    {"".join(links)}
</ul>

</body>
</html>
"""

    index_file = OUTPUT_DIR / "index.html"

    index_file.write_text(
        index_html,
        encoding="utf-8"
    )

    print(f"Generated: {index_file}")


if __name__ == "__main__":
    main()
