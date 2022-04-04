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
        "Last Tweet Intent": handle_last_tweet_intent,
    }

    try:
        query_result = request_json["queryResult"]
        user_intent = query_result["intent"]["displayName"]

        if user_intent in intent_dictionary:
            res = intent_dictionary[user_intent](query_result)
            answer_list = res[0]
            answer_tags = res[1]
            try:
                tag_mode = res[2]
            except Exception:
                tag_mode = 'all'
        else:
            answer_list = [
                "My engineers are working on this right now - thanks for talking to Elon Musk Bot"]
            answer_tags = ["Elon Musk"]
            tag_mode = 'all'

    except Exception as e:
        answer_list = [
            "My engineers are working on this right now - thanks for talking to Elon Musk Bot"]
        answer_tags = ["Elon Musk"]
        tag_mode = 'all'
    img = get_random_photo(answer_tags, tag_mode)

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
