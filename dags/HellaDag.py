from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Fonksiyon tanımı
def hello_world():
    print("Hello World")

# Default argümanlar
default_args = {
    'owner': 'YusufCaymaz',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG tanımı
with DAG(
    dag_id='0-hello_world_dag',
    default_args=default_args,
    description='A simple HelloWorld Dag',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 11, 1),
    catchup=False,
    tags=['example','HelloWorld'],
) as dag:

    # Görev tanımı
    hello_task = PythonOperator(
        task_id='hello_world_task',
        python_callable=hello_world,
    )

    hello_task
