from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag1 = DAG(
    'show_full_dag',
    default_args=default_args,
    start_date=datetime(2020, 1, 1),
    schedule_interval=timedelta(2)
)
t1 = BashOperator(
    task_id='echo_1',
    bash_command='echo 1',
    dag=dag1
)
t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    dag=dag1
)
t3 = BashOperator(
    task_id='echo_2',
    bash_command='echo 2',
    dag=dag1
)
t2.set_upstream(t1)
t3.set_upstream(t1)
