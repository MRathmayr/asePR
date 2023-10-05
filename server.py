import sys

import psycopg2
import psycopg2.extras
import flask
import json
import requests
from flask import Flask, request, jsonify, make_response

conn = None
cur = None


test_data = [{'id': 1, 'name': 'Ashley'}, {'id': 2, 'name': 'Kate'}, {'id': 3, 'name': 'Joe'}]
nextEmployeeID = 4

app = Flask(__name__)


def get_employee_by_id(id: int):
    return next((e for e in test_data if e['id'] == id), None)


@app.route("/employees/<int:id>", methods=["GET", "POST", "PUT", "DELETE"])
def stage_1(id: int):

    if request.method == "GET":

        employee = get_employee_by_id(id)

        if employee is None:
            return make_response(jsonify("Error"), 404)

        return make_response(jsonify(employee), 201)

    if request.method == "POST":

        received_data = json.loads(request.data)

        global nextEmployeeID
        received_data["id"] = nextEmployeeID
        nextEmployeeID += 1
        test_data.append(received_data)

        return make_response(jsonify("Success"), 201)

    if request.method == "PUT":

        employee = get_employee_by_id(id)

        if employee is None:
            return make_response(jsonify("Error"), 404)

        received_data = json.loads(request.data)
        employee.update(received_data)
        return make_response(jsonify(employee), 201)

    if request.method == "DELETE":

        employee = get_employee_by_id(id)

        if employee is None:
            return make_response("Employee does not exist", 404)

        test_data.remove(employee)
        return make_response(jsonify(employee, 201))


@app.route("/employees", methods=["GET"])
def stage_1_get_all():
    response = make_response(jsonify(test_data), 201)
    return response


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
    app.run()
