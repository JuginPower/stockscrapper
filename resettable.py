from stockmodels import Datamanager
from datetime import datetime


new_data = []
dm = Datamanager()
rough_data = dm.select("SELECT * FROM indiz_price")
actual_year = datetime.now().year

for item in rough_data:
    new_item = tuple([item[1], item[2], item[3]])
    new_data.append(new_item)

dm.query("TRUNCATE TABLE indiz_price")
dm.query(f"""CREATE TABLE indiz_price_{actual_year} (
         id int(255) primary key autoincrement not null, 
         indiz_id int(11),
         price double(7,2),
         zeit datetime)""")

inserted_rows = dm.query(f"INSERT INTO indiz_price{actual_year} (indiz_id, price, zeit) VALUES (%s, %s, %s)", new_data)
print("Rows inserted:", inserted_rows)
# testen