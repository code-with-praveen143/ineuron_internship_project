import anvil.server
import time
from urllib.request import urlopen
import pandas as pd
import pickle
import warnings

warnings.filterwarnings('ignore')
def app_func():
    anvil.server.connect('XFYQ3CHMJT4KDIKHK5L3L6U2-Z3Q5PLFWEGEDIH4Y')
    @anvil.server.callable

    def pred(online_order,book_table,votes,location,rest_type,cuisines,cost,menu_item):
        path = urlopen(r'https://github.com/code-with-praveen143/Zomato_Restaurant_Rating_Prediction/blob/master/model.pkl')

        cols = ['online_order','book_table','votes','location','rest_type','cuisines','cost','menu_item']

        pipeline = pickle.load(path)
        
        x = [0 for i in range(1,9)]
        x[0] = online_order
        x[1] = book_table
        x[2] = votes
        x[3] = location
        x[4] = rest_type
        x[5] = cuisines
        x[6] = cost
        x[7] = menu_item

        test_row = pd.DataFrame(x).transpose()
        test_row.columns = cols
        result = pipeline.predict(test_row)
        time.sleep(2)

        return round(result[0],0)

    anvil.server.wait_forever()