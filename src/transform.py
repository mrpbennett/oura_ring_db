import logging
from datetime import datetime

import psycopg2

db = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="192.168.5.52",
)


# https://api.ouraring.com/v2/usercollection/sleep


# TABLE - sleep_daily
def get_daily_sleep(data):

    for row in data["data"]:

        data = {
            "id": row["id"],
            "awake_time": row["awake_time"],
            "deep_sleep_duration": row["deep_sleep_duration"],
            "efficiency": row["efficiency"],
            "latency": row["latency"],
            "light_sleep_duration": row["light_sleep_duration"],
            "rem_sleep_duration": row["rem_sleep_duration"],
            "restless_periods": row["restless_periods"],
            "time_in_bed": row["time_in_bed"],
            "total_sleep_duration": row["total_sleep_duration"],
            "type": row["type"],
            "day": row["day"],
        }

        try:
            with db as conn:
                with conn.cursor() as curs:
                    curs.execute(
                        """
                            INSERT INTO oura_ring.sleep_daily 
                            (id, awake_time, deep_sleep_duration, efficiency, latency, light_sleep_duration, rem_sleep_duration, restless_periods, time_in_bed, total_sleep_duration, type, day) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                        (
                            data["id"],
                            data["awake_time"],
                            data["deep_sleep_duration"],
                            data["efficiency"],
                            data["latency"],
                            data["light_sleep_duration"],
                            data["rem_sleep_duration"],
                            data["restless_periods"],
                            data["time_in_bed"],
                            data["total_sleep_duration"],
                            data["type"],
                            data["day"],
                        ),
                    )
        except Exception as e:
            logging.error(e)


# TABLE - sleep_readiness
def get_daily_readiness(data):

    for row in data["data"]:

        data = {
            "id": row["id"],
            "activity_balance": row["readiness"]["contributors"]["activity_balance"],
            "body_temperature": row["readiness"]["contributors"]["body_temperature"],
            "hrv_balance": row["readiness"]["contributors"]["hrv_balance"],
            "previous_day_activity": row["readiness"]["contributors"][
                "previous_day_activity"
            ],
            "previous_night": row["readiness"]["contributors"]["previous_night"],
            "recovery_index": row["readiness"]["contributors"]["recovery_index"],
            "resting_heart_rate": row["readiness"]["contributors"][
                "resting_heart_rate"
            ],
            "sleep_balance": row["readiness"]["contributors"]["sleep_balance"],
            "score": row["readiness"]["score"],
            "day": row["day"],
        }

        try:
            with db as conn:
                with conn.cursor() as curs:
                    curs.execute(
                        """
                            INSERT INTO oura_ring.sleep_readiness
                            (id, activity_balance, body_temperature, hrv_balance, previous_day_activity, previous_night, recovery_index, resting_heart_rate, sleep_balance, score, day) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                        (
                            data["id"],
                            data["activity_balance"],
                            data["body_temperature"],
                            data["hrv_balance"],
                            data["previous_day_activity"],
                            data["previous_night"],
                            data["recovery_index"],
                            data["resting_heart_rate"],
                            data["sleep_balance"],
                            data["score"],
                            data["day"],
                        ),
                    )
        except Exception as e:
            logging.error(e)


# TABLE - sleep_hrv
def get_hrv_from_daily_sleep(data):

    for row in data["data"]:
        hrv = row["hrv"]

        data = {
            "items": hrv["items"],
            "timestamp": hrv["timestamp"],
        }

        timestamp = datetime.fromisoformat(data["timestamp"])

        for value in data["items"]:
            if value is not None:
                try:
                    with db as conn:
                        with conn.cursor() as curs:
                            curs.execute(
                                "INSERT INTO oura_ring.sleep_hrv (value, timestamp) VALUES (%s, %s)",
                                (value, timestamp),
                            )
                except Exception as e:
                    logging.error(e)


# TABLE - sleep_heart_rate
def get_heart_rate_from_daily_sleep(data):

    for row in data["data"]:
        heart_rate = row["heart_rate"]

        data = {
            "items": heart_rate["items"],
            "timestamp": heart_rate["timestamp"],
        }

        timestamp = datetime.fromisoformat(data["timestamp"])

        for value in data["items"]:
            if value is not None:
                try:
                    with db as conn:
                        with conn.cursor() as curs:
                            curs.execute(
                                "INSERT INTO oura_ring.sleep_heart_rate (value, timestamp) VALUES (%s, %s)",
                                (value, timestamp),
                            )
                except Exception as e:
                    logging.error(e)


# https://api.ouraring.com/v2/usercollection/daily_spo2


# TABLE - daily_blood_oxygen
def get_daily_blood_oxygen(data):

    for row in data["data"]:

        data = {
            "id": row["id"],
            "spo2_percentage": row["spo2_percentage"]["average"],
            "day": row["day"],
        }

        try:
            with db as conn:
                with conn.cursor() as curs:
                    curs.execute(
                        """
                            INSERT INTO oura_ring.daily_blood_oxygen
                            (id, spo2_percentage, day) VALUES (%s, %s, %s)""",
                        (
                            data["id"],
                            data["spo2_percentage"],
                            data["day"],
                        ),
                    )
        except Exception as e:
            logging.error(e)


# https://api.ouraring.com/v2/usercollection/daily_stress


# TABLE - daily_stress
def get_daily_stress(data):

    for row in data["data"]:

        data = {
            "id": row["id"],
            "day": row["day"],
            "stress_high": row["stress_high"],
            "recovery_high": row["recovery_high"],
            "day_summary": row["day_summary"],
        }

        try:
            with db as conn:
                with conn.cursor() as curs:
                    curs.execute(
                        """
                            INSERT INTO oura_ring.daily_stress
                            (id, stress_high, recovery_high, day_summary, day) VALUES (%s, %s, %s, %s, %s)""",
                        (
                            data["id"],
                            data["stress_high"],
                            data["recovery_high"],
                            data["day_summary"],
                            data["day"],
                        ),
                    )
        except Exception as e:
            logging.error(e)


# https://api.ouraring.com/v2/usercollection/daily_activity

# TABLE - daily_activity


def get_daily_activity(data):

    for row in data["data"]:

        data = {
            "id": row["id"],
            "day": row["day"],
            "score": row["score"],
            "active_calories": row["active_calories"],
            "target_calories": row["target_calories"],
            "resting_time": row["resting_time"],
            "sedentary_time": row["sedentary_time"],
            "steps": row["steps"],
            "target_calories": row["target_calories"],
        }

        try:
            with db as conn:
                with conn.cursor() as curs:
                    curs.execute(
                        """
                            INSERT INTO oura_ring.daily_activity
                            (id, score, active_calories, target_calories, resting_time, sedentary_time, steps,day) VALUES (%s, %s, %s, %s, %s,%s,%s)""",
                        (
                            data["id"],
                            data["score"],
                            data["active_calories"],
                            data["target_calories"],
                            data["resting_time"],
                            data["sedentary_time"],
                            data["steps"],
                            data["day"],
                        ),
                    )
        except Exception as e:
            logging.error(e)
