from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def Hello():
    return "Hello"

def World():
    return "World"

default_args = {
    'owner': 'YusufCaymaz',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id = '0-hello_to_world_dag',
    default_args = default_args,
    description = 'DAG Example that communicates two tasks with each other',
    schedule_interval = timedelta(days=1),
    start_date=datetime(2023,11,1),
    catchup = False,
    tags = ['example','Hello2World'],
) as dag:
    #Task
    hello_task = PythonOperator(
        task_id = 'HelloTask',
        python_callable = Hello,
    )

    world_task = PythonOperator(
        task_id = 'WorldTask',
        python_callable = World,
    )

    hello_task >> world_task

