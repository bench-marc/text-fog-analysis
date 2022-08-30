import textstat
import text_analysis as ta
import mysql.connector as mysql

my_db = mysql.connect (
    user = "leakraus",
    password = "LeaK",
    database = "gunning_fog_index"
)
my_cursor = my_db.cursor() 

def insert_data_in_mysql(text:list):
    for i in range(len(text)):
        if key_already_exists_in_database(text[i]['key']) == False:
            key = text[i]["key"]
            title = text[i]["title"]
            description_index = textstat.gunning_fog(text[i]["description"])
            if text[i]["response"] == None:
                response_index = 0
            else:
                response_index = textstat.gunning_fog(text[i]["response"])  
            if text[i]["conclusion"] == None:
                conclusion_index = 0
            else:
                conclusion_index = textstat.gunning_fog(text[i]["conclusion"])  
                
            val = f'"{key}", "{title}", "{description_index}", "{response_index}", "{conclusion_index}"'
            sql = f"INSERT INTO gunningfogindex(kam_key, title, description_index, response_index, conclusion_index) \
            VALUES({val});"
            
            my_cursor.execute(sql)
            my_cursor.execute("COMMIT;")
      
        
def key_already_exists_in_database(key:int):
    my_cursor.execute(f'SELECT count(*) FROM gunningfogindex WHERE kam_key = "{key}";')
    result = my_cursor.fetchone()[0]
    if result == 0:
        return False
    else:
        return True        
        
if __name__ == "__main__":
    text = ta.reading_data_from_xlsx_file("Textanalyse.xlsx")
    print(insert_data_in_mysql(text))
        