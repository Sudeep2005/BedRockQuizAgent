import json
import os
import urllib.request
import urllib.error


def lambda_handler(event, context):
    print("✅ Entered QuizCreator Lambda for Bedrock Agent")
    print("Event structure received:")
    print(json.dumps(event, indent=2))

    # Extract search term
    search_term = None
    if "parameters" in event:
        for param in event["parameters"]:
            if param.get("name") == "search_term":
                search_term = param.get("value")
                break

    if not search_term:
        return format_bedrock_response(event, 400, {"error": "search_term is required"})

    # Astra DB config
    astra_token = os.environ.get("astra_token")
    astra_endpoint = os.environ.get("astra_endpoint")
    keyspace = os.environ.get("keyspace", "default_keyspace")
    collection = os.environ.get("collection", "quizrag")

    if not astra_endpoint or not astra_token:
        return format_bedrock_response(event, 500, {"error": "Missing Astra DB credentials"})

    api_url = f"{astra_endpoint}/api/json/v1/{keyspace}/{collection}"

    # Query payload
    query_data = {
        "find": {
            "sort": {"$vectorize": search_term},
            "projection": {"$vectorize": 1},
            "options": {"limit": 5, "includeSimilarity": True},
        }
    }

    try:
        headers = {
            "Content-Type": "application/json",
            "X-Cassandra-Token": astra_token,
        }

        req = urllib.request.Request(
            api_url, data=json.dumps(query_data).encode("utf-8"), headers=headers, method="POST"
        )

        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))

        clean_results = []
        if "data" in result and "documents" in result["data"]:
            for doc in result["data"]["documents"]:
                if "$vectorize" in doc:
                    clean_results.append(doc["$vectorize"])

        return format_bedrock_response(
            event,
            200,
            {
                "search_term": search_term,
                "results": clean_results,
                "result_count": len(clean_results),
            },
        )

    except urllib.error.HTTPError as e:
        return format_bedrock_response(event, 500, {"error": f"Astra DB request failed: {str(e)}"})

    except Exception as e:
        return format_bedrock_response(event, 500, {"error": str(e)})


def format_bedrock_response(event, status_code, body):
    """Format response as per Bedrock Agent protocol"""
    return {
        "messageVersion": "1.0",
        "response": {
            "actionGroup": event.get("actionGroup", "QuizRAGAction"),
            "apiPath": event.get("apiPath", "/search"),
            "httpMethod": event.get("httpMethod", "POST"),
            "httpStatusCode": status_code,
            "responseBody": {
                "application/json": {
                    "body": str(body) if isinstance(body, str) else json.dumps(body)
                }
            },
        },
    }
