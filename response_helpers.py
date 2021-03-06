import json


response_headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "GET,OPTIONS,POST"
}


class InvalidTokenError(Exception):
    pass


class ExpiredTokenError(Exception):
    pass


options_response = {
    "statusCode": 200,
    "headers": response_headers,
    "body": json.dumps({"message": "successful options response"})
}


forbidden_action = {
    "statusCode": 403,
    "headers": response_headers,
    "body": json.dumps({"error": "hmm we dont let this"})
}


invalid_token = {
    "statusCode": 403,
    "headers": response_headers,
    "body": json.dumps({"error": "invalid id token"})
}


expired_id_token = {
    "statusCode": 403,
    "headers": response_headers,
    "body": json.dumps({"error": "expired id token"})
}


missing_files = {
    "statusCode": 400,
    "headers": response_headers,
    "body": json.dumps({"error": "missing files"})
}

max_file_size_exceeded = {
    "statusCode": 400,
    "headers": response_headers,
    "body": json.dumps({"error": "max file size limit exceeded"})
}

missing_file_name = {
    "statusCode": 400,
    "headers": response_headers,
    "body": json.dumps({"error": "missing file name"})
}


missing_file_contents = {
    "statusCode": 400,
    "headers": response_headers,
    "body": json.dumps({"error": "missing file contents"})
}


invalid_signature = {
    "statusCode": 400,
    "headers": response_headers,
    "body": json.dumps({"error": "invalid stripe signature"})
}


unknown_event_type = {
    "statusCode": 400,
    "headers": response_headers,
    "body": json.dumps({"error": "unknown event type"})
}

invalid_request = {
    "statusCode": 400,
    "headers": response_headers,
    "body": json.dumps({"error": "invalid request format"})
}

invalid_checkout_session = {
    "statusCode": 400,
    "headers": response_headers,
    "body": json.dumps({"error": "invalid checkout session"})
}

incorrect_price = {
    "statusCode": 400,
    "headers": response_headers,
    "body": json.dumps({"error": "incorrect price"})
}

