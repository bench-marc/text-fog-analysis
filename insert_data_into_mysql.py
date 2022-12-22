
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
            gf_description_index = textstat.gunning_fog(text[i]["description"])
            fre_description_index = textstat.flesch_reading_ease(text[i]["description"])
            if text[i]["response"] != None:
                gf_response_index = textstat.gunning_fog(text[i]["response"])
            else:
                gf_response_index = 0 
            if text[i]["response"] != None:
                fre_response_index = textstat.flesch_reading_ease(text[i]["response"])
            else:
                fre_response_index = 0     
            if text[i]["conclusion"] != None:
                gf_conclusion_index = textstat.gunning_fog(text[i]["conclusion"])
            else:
                gf_conclusion_index =  0
            if text[i]["conclusion"] != None:
                fre_conclusion_index = textstat.flesch_reading_ease(text[i]["conclusion"])
            else:
                fre_conclusion_index =  0    
            val = f'"{key}", "{title}", "{gf_description_index}", "{fre_description_index}", "{gf_response_index}", "{fre_response_index}", "{gf_conclusion_index}", "{fre_conclusion_index}"'
            sql = f"INSERT INTO gunningfogindex(kam_key, title, gunning_fog_description_index, flesch_reading_description_index, gunning_fog_response_index, flesch_reading_response_index, gunning_fog_conclusion_index, flesch_reading_conclusion_index) VALUES({val});"
            update_gf_response = "UPDATE gunningfogindex SET gunning_fog_response_index = NULL WHERE gunning_fog_response_index  = 0;"
            update_gf_conclusion = "UPDATE gunningfogindex SET gunning_fog_conclusion_index = NULL WHERE gunning_fog_conclusion_index  = 0;"
            update_fre_response = "UPDATE gunningfogindex SET flesch_reading_response_index = NULL WHERE flesch_reading_response_index  = 0;"
            update_fre_conclusion = "UPDATE gunningfogindex SET flesch_reading_conclusion_index = NULL WHERE flesch_reading_conclusion_index  = 0;"
            
            my_cursor.execute(sql)
            my_cursor.execute(update_gf_response)
            my_cursor.execute(update_gf_conclusion)
            my_cursor.execute(update_fre_response)
            my_cursor.execute(update_fre_conclusion)
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