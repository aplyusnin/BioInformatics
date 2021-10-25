# Setting location for Airflow home
export AIRFLOW_HOME=~/airflow/

# creating new virtual environment
sudo apt install python3.8-venv
python3 -m venv .venv

# switch to this environment
source .venv/bin/activate

# installing Airflow itself
pip install apache-airflow

# initialization of Airflow database 
airflow db init

# creating local user
airflow users create \
          --username admin \
          --firstname FIRST_NAME \
          --lastname LAST_NAME \
          --role Admin \
          --email admin@example.org


# Starting Web UI on localhost:8080
airflow webserver -p 8080

# Starting scheduler
airflow scheduler

# Future work can be done inside web UI
