from airflow import DAG
from airflow.operators.dummy import DummyOperator
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
    'show_what_is_dag',
    start_date=datetime(2020, 1, 1),
    default_args=default_args,
    schedule_interval=timedelta(days=1)
)
t1 = DummyOperator(task_id='a', dag=dag1)
t2 = DummyOperator(task_id='b', dag=dag1)
t3 = DummyOperator(task_id='c', dag=dag1)
t4 = DummyOperator(task_id='d', dag=dag1)
t5 = DummyOperator(task_id='e', dag=dag1)
t2.set_upstream(t1)
t3.set_upstream(t1)
t4.set_upstream(t1)
t4.set_upstream(t2)
t4.set_upstream(t3)
t5.set_upstream(t1)
t5.set_upstream(t3)
t5.set_upstream(t4)
