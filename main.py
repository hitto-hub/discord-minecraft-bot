import os
# Pycordを読み込む
import discord
import dotenv
import subprocess

# .envファイルを読み込む
dotenv.load_dotenv()
# アクセストークンを設定
token = str(os.getenv("TOKEN"))
# cwdを設定
cwd = str(os.getenv("CWD"))
# SERVER_FILE_PATHを設定
server_file_path = str(os.getenv("SERVER_FILE_PATH"))

# Botの大元となるオブジェクトを生成する
bot = discord.Bot(
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
        activity=discord.Game("Minecraft"),  # "〇〇をプレイ中"の"〇〇"を設定,
)

# 起動時に自動的に動くメソッド
@bot.event
async def on_ready():
    # 起動すると、実行したターミナルに"Hello!"と表示される
    print("Hello!")

# コマンドを定義する
# startコマンド
@bot.command(name="start", description="サーバーを起動させるコマンドです。")
async def start(ctx: discord.ApplicationContext):
    try:
        res = subprocess.check_output("screen -ls", shell=True, encoding="utf-8")
        print(res)
        # すでに起動しているかどうかを確認
        if "mcServer" in res:
            print("既に実行済み")
            await ctx.respond("既に実行されてるかもです！！！")
            return
        else:
            print("実行されてないが、ほかのプロセスが実行されている")
    except Exception as e:
        print(f"Error: {e}")
        
    print("start")
    try:
        srartCommand = "screen -dmS mcServer java -jar " + cwd +"/" + server_file_path
        subprocess.call(srartCommand, shell=True, cwd=cwd)
        await ctx.respond("起動コマンドを送信しました！")
    except Exception as e:
        print(f"Error: {e}")
        await ctx.respond(e)

# stopコマンド
@bot.command(name="stop", description="サーバーを停止させるコマンドです。")
async def stop(ctx: discord.ApplicationContext):
    try:
        res = subprocess.check_output("screen -ls", shell=True, encoding="utf-8")
        print(res)
        # すでに起動しているかどうかを確認
        if "mcServer" in res:
            await ctx.respond("サーバーを停止します！")
            try:
                res = subprocess.check_output("screen -S mcServer -X stuff 'stop\n'", shell=True, encoding="utf-8")
                await ctx.respond("サーバーを停止しました！")
                return
            except Exception as e:
                print(f"Error: {e}")
                await ctx.respond("サーバーを停止できませんでした！")
                await ctx.respond("error: " + e)
                return
        else:
            print("実行されてないが、ほかのプロセスが実行されている")
            await ctx.respond("サーバーは起動していません！")
            return
    except Exception as e:
        print(f"Error: {e}")
        await ctx.respond("サーバーは起動していません！")

# whitelistコマンド
# subcommandがlistの場合playerはNone
# subcommandがaddの場合playerは必須
# subcommandがremoveの場合playerは必須
@bot.command(name="whitelist", description="whitelist <subcommand> <player>コマンドを実行します。")
async def whitelist(ctx: discord.ApplicationContext
                    ,sub_command: discord.Option(str, "subcommandを選択してください。", choices=["add", "remove", "list"])
                    ,player: discord.Option(str, "プレイヤー名を入力してください。add, removeの場合は必須です。", required=False)):
    if sub_command == "add":
        try:
            res = subprocess.check_output("screen -ls", shell=True, encoding="utf-8")
            print(res)
            # すでに起動しているかどうかを確認
            if "mcServer" in res:
                if player == None:
                    await ctx.respond("プレイヤー名を入力してください。")
                    return
                try:
                    res = subprocess.check_output("screen -S mcServer -X stuff 'whitelist add " + player + "\n'", shell=True, encoding="utf-8")
                    await ctx.respond(player + "をwhitelistに追加しました！")
                    return
                except Exception as e:
                    print(f"Error: {e}")
                    await ctx.respond(player + "をwhitelistに追加できませんでした")
                    await ctx.respond("error: " + e)
                    return
            else:
                print("実行されてないが、ほかのプロセスが実行されている")
                await ctx.respond("サーバーは起動していません。起動してから実行してください。")
                return
        except Exception as e:
            print(f"Error: {e}")
            await ctx.respond("サーバーは起動していません。起動してから実行してください。")
            return
    elif sub_command == "remove":
        try:
            res = subprocess.check_output("screen -ls", shell=True, encoding="utf-8")
            print(res)
            # すでに起動しているかどうかを確認
            if "mcServer" in res:
                if player == None:
                    await ctx.respond("プレイヤー名を入力してください。")
                    return
                try:
                    res = subprocess.check_output("screen -S mcServer -X stuff 'whitelist remove " + player + "\n'", shell=True, encoding="utf-8")
                    await ctx.respond(player + "をwhitelistから削除しました！")
                    return
                except Exception as e:
                    print(f"Error: {e}")
                    await ctx.respond(player + "をwhitelistから削除できませんでした")
                    await ctx.respond("error: " + e)
                    return
            else:
                print("実行されてないが、ほかのプロセスが実行されている")
                await ctx.respond("サーバーは起動していません。起動してから実行してください。")
                return
        except Exception as e:
            print(f"Error: {e}")
            await ctx.respond("サーバーは起動していません。起動してから実行してください。")
            return
    elif sub_command == "list":
        try:
            res = subprocess.check_output("screen -ls", shell=True, encoding="utf-8")
            print(res)
            # すでに起動しているかどうかを確認
            if "mcServer" in res:
                try:
                    res = subprocess.check_output("screen -S mcServer -X stuff 'whitelist list\n'", shell=True, encoding="utf-8")
                    # 実行結果を取得
                    res_list = subprocess.check_output("tail -n 1 " + cwd + "/logs/latest.log", shell=True, encoding="utf-8")
                    print(res_list)
                    await ctx.respond(res_list)
                    return
                except Exception as e:
                    print(f"Error: {e}")
                    await ctx.respond("whitelist listを実行できませんでした")
                    await ctx.respond("error: " + e)
                    return
            else:
                print("実行されてないが、ほかのプロセスが実行されている")
                await ctx.respond("サーバーは起動していません。起動してから実行してください。")
                return
        except Exception as e:
            print(f"Error: {e}")
            await ctx.respond("サーバーは起動していません。起動してから実行してください。")
            return
    else:
        await ctx.respond("subcommandを選択してください。")
        return
    
bot.run(token)
