import sys

import psycopg2
import psycopg2.extras
import flask
import json
import requests

conn = None
cur = None


def stage1():

    connect_to_database()
    token = get_token()

    # get first testcase and link
    test_case = get_testcase(stage=1, testcase_no=1, token=token)
    new_test_link = "https://reset.inso.tuwien.ac.at/ase/<scenarioPrefix>/assignment/11909908/stage/1/testcase/1?token=" + token
    while True:

        # solve problem, update database and create return dict
        computation_result = test_case

        # post result
        result = post_result(url=new_test_link, value=computation_result)

        # if program progresses here, successful test, need to get new test_case
        # if result contains congratulations, all tests finished and exit
        new_test_link = str(result["linkToNextTask"])
        if "Congratulations" in new_test_link:
            break

        # get new testcase
        test_case = get_testcase_directly(new_test_link)


    close_connection()


def get_token():
    response = json.loads(
        requests.get("https://reset.inso.tuwien.ac.at/ase/<scenarioPrefix>/assignment/11909908/token").json())
    return response["token"]


def get_testcase(stage, testcase_no, token):
    response = requests.get(
        "https://reset.inso.tuwien.ac.at/ase/<scenarioPrefix>/assignment/11909908/stage/" + str(
            stage) + "/testcase/" + str(
            testcase_no) + "?token=" + str(token))
    if response.status_code == 404:
        print("404 error with testcase " + str(testcase_no))
        sys.exit(1)
    return json.loads(response.json())


def get_testcase_directly(link):
    response = requests.get(link)
    if response.status_code == 404:
        print("404 error with testcase " + str(response))
        sys.exit(1)
    return json.loads(response.json())


def post_result(url, value: dict):
    value_json = json.dumps(value)
    response = requests.post(url, value_json)
    if response.status_code != 202:
        print("ERROR: " + str(response))
        sys.exit(1)
    return json.loads(response.json())


def connect_to_database():
    hostname = "x"
    database = "x"
    username = "x"
    pwd = "x"
    port_id = 1

    try:
        global conn, cur
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )

        cur = conn.cursor()
    except Exception as error:
        print(error)


def close_connection():
    cur.close()
    conn.close()


def operate_on_database(script: str):
    cur.execute(script)
    ret_val = cur.fetchall()
    conn.commit()
    return ret_val


if __name__ == '__main__':
    stage1()
