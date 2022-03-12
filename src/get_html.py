import pandas as pd
import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

# pyppeteer→BeautifulSoup→pandasでHTMLのtableを読み込む
async def get_html():
	try:
		# pyppeteer
		browser = await launch()
		page = await browser.newPage()
		response = await page.goto("https://スクレイピングしたいWebサイトのURL")
		html = await page.content()
		# BeautifulSoup
		soup = BeautifulSoup(html, "lxml")
		tables = soup.find_all("table")
		# pandas
		dfs = pd.read_html(str(tables))

	except:
		#エラー処理を書く
		print("Error")

	else:
		# pandasのデータフレーム処理を書く
		print(dfs)

	finally:
		# ブラウザクローズしないとメモリリークするので注意
		await browser.close()

# get_html関数呼び出し
asyncio.get_event_loop().run_until_complete(get_html())
