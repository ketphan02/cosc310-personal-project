from intent_handlers import *
from flask import jsonify
from flickr import get_random_photo

def cloud_function(request_json):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    # request_json = request.get_json()
    print(f"DEBUG: {request_json}")

    intent_dictionary = {
        "What Company Does Intent": handle_what_company_intent,
        "Work at SpaceX Intent - custom": handle_WorkatSpaceXIntent_followup,
        "Crypto Advice Intent": handle_crypto_advice_intent,
        "What is Crypto Intent": handle_what_is_crypto_intent,
        "Billionaire Tax Intent": handle_billionaire_tax_intent,
        "Daily Routine Intent": handle_daily_routine_intent,
        "Neuralink Applications Intent - custom": handle_NeuralinkAppIntent_followup,
        "Fight Putin Intent": handle_fight_putin_intent,
        "Stand With Ukraine Intent": handle_stand_with_ukraine_intent,
    }

    try:
        query_result = request_json["queryResult"]
        user_intent = query_result["intent"]["displayName"]

        if user_intent in intent_dictionary:
            print(intent_dictionary[user_intent](query_result))
            
            answer_list, answer_tags = intent_dictionary[user_intent](query_result)
        else:
            answer_list = [
                "My engineers are working on this right now - thanks for talking to Elon Musk Bot"]
            answer_tags = ["Elon Musk"]

    except:
        answer_list = [
            "My engineers are working on this right now - thanks for talking to Elon Musk Bot"]
        answer_tags = ["Elon Musk"]

    print(answer_tags)

    img = get_random_photo(answer_tags)
    answer = {
        "fulfillmentMessages": [
            {
                "image": {
                    "imageUri": img if img else get_random_photo(["Elon Musk"]),
                }
            }, {
                "text": {
                    "text": answer_list
                }
            }
        ],
    }

    return jsonify(answer)
