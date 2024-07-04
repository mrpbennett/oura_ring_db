import logging

from extract import (
    get_usercollection_daily_activity,
    get_usercollection_daily_sleep,
    get_usercollection_daily_spo2,
    get_usercollection_sleep,
    get_usercollection_sleep_time,
    get_usercollection_stress,
    get_usercollection_workout,
)
from transform import (
    get_blood_oxygen,
    get_daily_activity,
    get_daily_activity_contributors,
    get_heart_rate,
    get_hrv,
    get_readiness,
    get_sleep,
    get_sleep_score,
    get_sleep_time,
    get_stress,
    get_workout,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - line:%(lineno)d - %(filename)s:%(funcName)s -> %(message)s",
)

daily_activity = get_usercollection_daily_activity()
daily_sleep = get_usercollection_daily_sleep()
sleep = get_usercollection_sleep()
sleep_time = get_usercollection_sleep_time()
stress = get_usercollection_stress()
blood_o2 = get_usercollection_daily_spo2()
workout = get_usercollection_workout()


def main():

    # https://api.ouraring.com/v2/usercollection/daily_activity
    # TABLE - daily_activity
    if get_daily_activity(daily_activity):
        logging.info("daily_activity table has been updated")

    # TABLE - daily_activity_contributors
    if get_daily_activity_contributors(daily_activity):
        logging.info("daily_activity_contributors table has been updated")

    # https://cloud.ouraring.com/v2/usercollection/daily_sleep
    # TABLE - sleep_score
    if get_sleep_score(daily_sleep):
        logging.info("sleep_score table has been updated")

    # https://api.ouraring.com/v2/usercollection/sleep
    # TABLE - sleep
    if get_sleep(sleep):
        logging.info("sleep table has been updated")
    # TABLE - hrv
    if get_hrv(sleep):
        logging.info("hrv table has been updated")
    # TABLE - heart_rate
    if get_heart_rate(sleep):
        logging.info("heart_rate table has been updated")
    # TABLE - readiness
    if get_readiness(sleep):
        logging.info("readiness table has been updated")

    # https://cloud.ouraring.com/v2/usercollection/sleep_time
    # TABLE - sleep_time
    if get_sleep_time(sleep_time):
        logging.info("sleep_time table has been updated")

    # https://api.ouraring.com/v2/usercollection/daily_stress
    # TABLE - stress
    if get_stress(stress):
        logging.info("stress table has been updated")

    # https://api.ouraring.com/v2/usercollection/daily_spo2
    # TABLE - blood_oxygen
    if get_blood_oxygen(blood_o2):
        logging.info("blood_oxygen table has been updated")

    # https://cloud.ouraring.com/v2/usercollection/workout
    # TABLE - workout
    if get_workout(workout):
        logging.info("workout table has been updated")


if __name__ == "__main__":
    main()
