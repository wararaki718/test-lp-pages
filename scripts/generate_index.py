from pathlib import Path


PAGES_DIR = Path("pages")


def generate_index():
    lp_dirs = sorted(
        path
        for path in PAGES_DIR.iterdir()
        if path.is_dir() and (path / "index.html").exists()
    )

    cards = []

    for lp_dir in lp_dirs:
        name = lp_dir.name

        cards.append(
            f"""
            <li>
              <a href="./{name}/">
                {name}
              </a>
            </li>
            """
        )

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sample LPs</title>
</head>

<body>

  <h1>Sample LPs</h1>

  <p>
    このページは GitHub Actions によって自動生成されています。
  </p>

  <h2>LP一覧</h2>

  <ul>
    {"".join(cards)}
  </ul>

</body>
</html>
"""

    (PAGES_DIR / "index.html").write_text(
        html,
        encoding="utf-8"
    )


if __name__ == "__main__":
    generate_index()