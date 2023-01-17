"""Provides schema for retrieve analytics endpoint"""
from enums.enums import TimeTypes

RETRIEVE_ANALYTICS_BODY_SCHEMA = {
    'type': 'object',
    'required': ['user_id', 'time_type'],
    'properties': {
        'user_id': {
            'type': 'string',
            'minLength': 1,
        },
        'time_type': {
            'type': 'integer',
            'minimum': TimeTypes.get_enums_min_value(),
            'maximum': TimeTypes.get_enums_max_value(),
        },
    }
}
