from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.models import Variable

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
with DAG(
    dag_id="pipeline", start_date=datetime(2021, 1, 1), catchup=False, tags=["assignment"]
) as dag:

    referenceIndexing = BashOperator(task_id="Reference_Genome_input", do_xcom_push=True, bash_command="bwa index {{ params.reference }}")

    bwa = BashOperator(task_id="bwa_mem", do_xcom_push=True, bash_command= "bwa mem {{ params.reference }} {{ params.reads}} > {{ params.temp }}")
    
    samtools = BashOperator(task_id="samtools", do_xcom_push=True, bash_command="echo $(samtools flagstat {{ params.temp }} | head -n 5 | tail -1 | grep -o -P '[0-9]*(\.[0-9]*)?(?=%)')") 

    evaluation = BashOperator(task_id="evaluation", bash_command='if (($(echo {{ ti.xcom_pull(task_ids="samtools") }}">90" | bc -l))); then\n  echo "OK"\nelse\n  echo "Not OK"\nfi')

    referenceIndexing >> bwa >> samtools >> evaluation
