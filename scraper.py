# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import sqlite3
import pandas as pd

conn = sqlite3.connect("selectfashion13.sqlite")
conn2 = sqlite3.connect("data.sqlite")

images = pd.read_sql("Select * from images",conn)
JigarKey = pd.read_sql("Select * from JigarKey",conn)
product = pd.read_sql("Select * from product",conn)

images.to_sql("images", conn2, if_exists='replace', index=False)
product.to_sql("product", conn2, if_exists='replace', index=False)
JigarKey.to_sql("JigarKey", conn2, if_exists='replace', index=False)

