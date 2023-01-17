from flask import Flask, request, jsonify
from flask_json_schema import JsonSchema, JsonValidationError

from database.every_day_analytics import EveryDayAnalytics
from enums.enums import TimeTypes
from misc.functions import TimeBasedIds
from misc.time import Time
from misc.week_analytics import WeekAnalytics
from schemas.retrieve_analytics import RETRIEVE_ANALYTICS_BODY_SCHEMA
from schemas.write_analytics import WRITE_ANALYTICS_BODY_SCHEMA

app = Flask(__name__)
schema = JsonSchema(app)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, ValueError):
        return jsonify(error=str(e)), 400
    if isinstance(e, Exception):
        return jsonify(error=str(e)), 400
    if isinstance(e, NotImplementedError):
        return jsonify(error=str(e)), 400
    return jsonify(error=str(e)), code


@app.errorhandler(JsonValidationError)
def schema_validation_error(e):
    """Schema errors handler"""
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@app.route('/analytics', methods=['POST'])
@schema.validate(RETRIEVE_ANALYTICS_BODY_SCHEMA)
def retrieve_analytics():
    user_id: str = request.json.get('user_id')
    time_type: int = request.json.get('time_type')
    if time_type == TimeTypes.Week.value:
        return WeekAnalytics.retrieve_week_analytics(user_id)
    if time_type == TimeTypes.Month.value:
        raise NotImplementedError("This time type is now available at the moment! Probably, it is not implemented!")
    raise ValueError("Something went wrong")


@app.route('/analytics/update', methods=['POST'])
@schema.validate(WRITE_ANALYTICS_BODY_SCHEMA)
def write_analytics():
    looser_data: dict = request.json.get('looser_data')
    winner_data: dict = request.json.get('winner_data')

    looser_id: str = looser_data.get('user_id')
    winner_id: str = winner_data.get('user_id')
    date = Time.get_date_now()

    looser_primary_key = TimeBasedIds.get_id(date, looser_id)
    winner_primary_key = TimeBasedIds.get_id(date, winner_id)

    looser_item = EveryDayAnalytics.find_item(looser_primary_key)
    winner_item = EveryDayAnalytics.find_item(winner_primary_key)

    items = [(looser_item, looser_data), (winner_item, winner_data)]
    EveryDayAnalytics.write_new_item_or_update_existing(items)
    return {"message": "Profile analytics were successfully updated!"}


if __name__ == '__main__':
    app.run()
