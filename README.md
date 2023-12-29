# Discord Minecraft Bot

## env
.env.exampleを参考に.envを作成してください。

## 起動

```bash
git clone https://github.com/hitto-hub/discord-minecraft-bot.git &&
cd discord-minecraft-bot &&
apt install python3.10-venv &&
python3 -m venv venv &&
. venv/bin/activate &&
pip install -r ./requirements.txt &&
python3 ./main.py
```

## コマンド
/start: サーバーを起動します。
/stop: サーバーを停止します。
/whitelist <username>: ホワイトリストに追加します。

## ライセンス
[MIT]

## 作者
hitto

## その他
気が向いたらwhitelistらへんの機能追加します。

This README.md was largely created by GitHub Copilot.
