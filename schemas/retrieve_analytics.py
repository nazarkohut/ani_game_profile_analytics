RETRIEVE_ANALYTICS_BODY_SCHEMA = {
    'type': 'object',
    'required': ['user_id', 'time_type'],
    'properties': {
        'user_id': {'type': 'string'},
        'time_type': {'type': 'integer'},
    }
}
