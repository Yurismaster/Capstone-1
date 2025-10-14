from typing import Any, Optional, Iterable, Sequence, Mapping, Dict, List, Tuple
from datetime import datetime
from pathlib import Path
import logging
import duckdb

/*creating tables*/
CREATE TABLE IF NOT EXISTS Events ()

CREATE TABLE IF NOT EXISTS Feature ()

CREATE TABLE IF NOT EXISTS Alert ()

CREATE TABLE IF NOT EXISTS Alert_Reasons ()


/*searching from the tables*/
def Find_Time(time_from, time_to):
	/*searching by time*/

def Find_App(app_pkg):
	/*searching by app name*/

def Find_TimeAndApp(app_pkg, time_from, time_to):
	/*searching by app name and specific time*/


/*security&training support*/
def View_Features_Training(app_pkg, t0, t1):
	/*Feature set view during training (feature columns extracted by time window)*/

def Show_Events(app_pkg):
	/*Show the complete event flow of an application (For troubleshooting)*/

def fn_Test_Features(alert_id):
	/*Sampling a subset of relevant features for a certain alarm to control query costs*/


/*Monitoring and maintenance*/
def _retryFailedImports():
	/*Automatic retry when data import fails*/

def _enforceIntegrityConstraints():
	/*Integrity check (time series, required columns, primary key/deduplication)*/

def _recordPerfStats(job_id, bytes_processed, duration_ms):
	/*Record data volume and time consumption, and support P50/P95/P99 indicator statistics*/


/*DAO interface*/
/*interface for backend*/
class dao:
	@staticmethod
	def Get_Alerts(t0, t1):
		/*return alert by time*/

	@staticmethod
	def Insert_Event(event_row):
		/*insert single event, with content verification*/

	@staticmethod
	def fn_Top3(alert_id):
		/*get top 3 alert reason*/



