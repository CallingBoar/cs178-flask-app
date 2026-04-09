#Bernardo Martinez

import boto3
from boto3.dynamodb.conditions import Key
from flask import render_template

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Countries"


def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def add_country_to_dynamo(item):
    """adds an item to the dynamo table"""
    table = get_table()
    response = table.put_item(Item = item)
    return response
