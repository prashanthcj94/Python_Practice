import pandas as pd
import matplotlib as md
import numpy
import json
import os

print(os.getcwd())
def read_excel_as_obj():
    excel_data_df = pd.read_excel(
        "C:\\Users\\prashanth.k.lv\\Documents\\Python_Practices\\Resource\\Simple_sample.xlsx", sheet_name="Details"
)
    print(list(excel_data_df.items()))
    json_str = excel_data_df.to_json(orient="records")
    json_object = json.loads(json_str)
    print(json_object)


read_excel_as_obj()