from robot.api import logger

ROBOT_LISTENER_API_VERSION = 3

def end_test(data, result):
    print("ALKU3!!!!!!!")
    logger.info("HERE!!!!!!!")
    logger.info(f"Test ended: {data.name}")
    logger.info(f"Passed: {result.passed}")
    logger.info(f"Message: {result.message}")
    
    if not result.passed:
        print("!!!" + result.message + "!!!")
        if str.lower("Should Be Equal As Strings") in str.lower(result.message):
            print("NOOOOOOOO!!!!")
            result.tags.add("testitagi")