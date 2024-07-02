import json

from extract import get_activity, get_blood_oxygen, get_sleep, get_stress
from transform import (
    get_daily_activity,
    get_daily_blood_oxygen,
    get_daily_readiness,
    get_daily_sleep,
    get_daily_stress,
    get_heart_rate_from_daily_sleep,
    get_hrv_from_daily_sleep,
)

sleep = json.loads(get_sleep())
stress = json.loads(get_stress())
blood_o2 = json.loads(get_blood_oxygen())
activity = json.loads(get_activity())


def main():

    # DAILY SLEEP DATA
    get_daily_sleep(sleep)
    get_daily_readiness(sleep)
    get_hrv_from_daily_sleep(sleep)
    get_heart_rate_from_daily_sleep(sleep)

    # DAILY STRESS DATA
    get_daily_stress(stress)

    # BLOOD OXYGEN DATA
    get_daily_blood_oxygen(blood_o2)

    # DAILY ACTIVITY DATA
    get_daily_activity(activity)


if __name__ == "__main__":
    main()
