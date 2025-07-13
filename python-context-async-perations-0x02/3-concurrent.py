import aiosqlite
import asyncio

db_path = '../data/users.db'

async def async_fetch_users():
	async with aiosqlite.connect(db_path) as conn:
		cursor = await conn.execute("SELECT * FROM users")
		results = await cursor.fetchall()
		return results

async def async_fetch_older_users():
	async with aiosqlite.connect(db_path) as conn:
		cursor = await conn.execute("SELECT * FROM users WHERE age > ?", (40,))
		results = await cursor.fetchall()
		return results

async def fetch_concurrently(): 	
	results_all, results_older = await asyncio.gather(async_fetch_users(), async_fetch_older_users())
	return results_all, results_older

all_users, older_users = asyncio.run(fetch_concurrently())

print("Output of 3 first users in the first query:")
for i, user in enumerate(all_users):
	print(f"{user}")
	if i == 2:
		break

print("Output of 3 first users in the second query:")
for i, user in enumerate(older_users):
	print(f"{user}")
	if i == 2:
		break