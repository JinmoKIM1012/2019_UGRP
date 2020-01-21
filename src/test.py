from mysql_ReadQuery import mysqlQuery
from similarity import *
from audio_input_speech_recognition import speechRecognitionByGoogle


test_text = speechRecognitionByGoogle()
query_data = mysqlQuery()
query_lst = [i[1] for i in query_data]
max_query = ''
max_sim = 0
for query in query_lst:
    sim_tmp = sim(test_text, query)
    if max_sim < sim_tmp:
        max_sim = sim_tmp
        max_query = query
print(max_query)
max_ind_query = [item[0] for item in query_data if item[1] == max_query]
print(max_ind_query)
