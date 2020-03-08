import json
from p_entry import optimize_portfolio

def lambda_handler(event, context):
    output = optimize_portfolio(event)
    return {
        'statusCode': 200,
        'body': output
    }
