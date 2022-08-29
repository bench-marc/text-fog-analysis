
import re
import openpyxl
import textstat


def reading_data_from_xlsx_file(file:str):
    dataframe = openpyxl.load_workbook(file)
    dataframe1 = dataframe.active
    data = ""
    for row in range(0, dataframe1.max_row):
        for col in dataframe1.iter_cols(0, dataframe1.max_column-1):
            print("" + str(col[row].value))

def text_editing(text:str):
   # test if there is a dot a the end of a sentence
   text.endswith(". ")
   # remove bullets
   text.replace("/[•\t]+/g", "")
   # Capitalize 
   text.capitalize()
   # what about numbers
        # gunning_fog_index runs with numbers as well, so i would say we leave them in. 
   # what about dates with dots
        # Sentences are ending normally with ". ". Dates do not have spaces between numbers --> regex 
   # ending sentences with ";" or ":"
   
   pass

def gunning_fog_index(text:str):
    return textstat.gunning_fog(text)

if __name__ == "__main__":
    print(text_editing("• Lea Kraus"))