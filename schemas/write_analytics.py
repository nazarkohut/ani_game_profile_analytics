USER_SCHEMA = {
    'type': 'object',
    'required': ['user_id', 'user_rating'],
    'properties': {
        'user_id': {
            'type': 'string',
            'minLength': 1
        },
        'user_rating': {
            'type': 'integer',
            'minimum': 0,
        },
    }
}

WRITE_ANALYTICS_BODY_SCHEMA = {
    'type': 'object',
    'required': ['looser_data', 'winner_data'],
    'properties': {
        'looser_data': USER_SCHEMA,
        'winner_data': USER_SCHEMA,
    },
}
