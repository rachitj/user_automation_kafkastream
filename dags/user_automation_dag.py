from datetime import datetime, timedelta, time
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import json
import logging
import requests
from kafka import KafkaProducer



def get_user_data():
    # code to stream user data from source to destination


    res = requests.get('https://randomuser.me/api/')
    def get_user_data():
        # code to stream user data from source to destination
        res = requests.get('https://randomuser.me/api/')
        res.encoding = 'utf-8'  # specify the encoding
        res = res.json()
        res = res['results'][0] 

        return res
    res = res.json()
    res = res['results'][0] 

    return res


def format_user_data(res):
    # code to format user data
    user_data = {
        'first_name': res['name']['first'],
        'last_name': res['name']['last'],
        'title': res['name']['title'],
        'gender': res['gender'],
        'username': res['login']['username'],
        'password': res['login']['password'],
        'phone': res['phone'],
        'cell': res['cell'],
        'dob': res['dob']['date'],
        'age': res['dob']['age'],
        'address': res['location']['street']['name'],
        'city': res['location']['city'],
        'state': res['location']['state'],
        'country': res['location']['country'],
        'postcode': res['location']['postcode'],
        'latitude': res['location']['coordinates']['latitude'],
        'longitude': res['location']['coordinates']['longitude'],
        'picture': res['picture']['large'],
        'email': res['email']
    }

    return user_data

def stream_user_data():
    import time

    producer = KafkaProducer(bootstrap_servers=['broker : 29092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'), max_block_ms=10000)
    current_time = time.time()

    while True:
            if time.time() > current_time + 120  :
                 break
            try: 
                res = get_user_data()
                res = format_user_data(res)
                producer.send('user_data', value=res)
                print('User data streamed successfully')
            except Exception as e:
                print('Error streaming user data n: {e}')
                continue
                 

default_args = {
    'owner': 'dataforgemaster',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 20, 7, 0),
    'catchup': False
}
    



with DAG('user_automation_dag',
         default_args=default_args,
         schedule_interval=timedelta(days=1),
         ) as dag:

    def print_hello():
        return 'Hello world!'

    def print_goodbye():
        return 'Goodbye!'

    run_this_first = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )

    task_stream_user_data = PythonOperator(
        task_id='stream_user_data',
        python_callable=stream_user_data
    )

    run_this_last = PythonOperator(
        task_id='print_goodbye',
        python_callable=print_goodbye
    )

    run_this_first >> task_stream_user_data >> run_this_last


if __name__ == '__main__':
    stream_user_data()


