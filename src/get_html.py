import pandas as pd
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# playwright→BeautifulSoup4→pandasでHTMLのtableを読み込む
def get_html(playwright):
	try:
		# playwright
		browser = playwright.chromium.launch()
		context  = browser.new_context()
		page = context.new_page()
		page.goto("https://スクレイピングしたいWebサイトのURL")
		html = page.content()
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
		page.close()
		context.close()
		browser.close()

# get_html関数呼び出し
with sync_playwright() as playwright:
	get_html(playwright)
