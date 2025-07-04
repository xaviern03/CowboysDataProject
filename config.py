BOOLEAN_COLUMNS = {
    "plays": ['is_running_clock', 'is_no_play', 'off_is_touchdown', 'no_huddle', 'is_play_action', 'off_has_man_in_motion', 'is_catchable', 'pass_breakup'],
    
    "offense": ['ball_carrier', 'catchable_target', 'reception', 'pass_touchdown', 'receiving_toucdown', 'interception', 'dropped_pass', 'presssure_allowed'
               'sack_allowed'],
    
    "defense": ['solo_tackle', 'assisted_tackle', 'missed_tackle', 'forced_fumble', 'fumble_recovery', 'batted_pass', 'pressure', 'def_target', 'reception_allowed',
                'forced_incompletion', 'pass_breakup', 'interception']
}

NUMERIC_BOUNDS = {
    "plays": {
        "drive": (1, None),
        "drive_play" : (1, None),
        "quarter": (1, 5),
        "down": (1, 4),
        "distance": (1, None),
        "off_score": (0, None),
        "def_score": (0, None),
        "off_timeouts_remaining": (0, 3),
        "def_timeouts_remaining": (0, 3),
        "time_to_throw": (0, None),
        "time_to_pressure": (0, None)
    },

    "offense": {},

    "defense": {
        "sack": (0, 2),
    },

    "games": {
        "vis_score_point_total": (0, None),
        "home_score_point_total": (0, None),
    }
}

UPPER_COLUMNS = {
    "offense": ['position', 'pass_route_name', 'pass_route_group'],
    "defense": ['position'],
    "plays": ['play_type', 'play_result', 'offensive_formation', 'off_qb_alignment', 'dropback_type', 'pass_direction', 'pass_rush_result', 'left_route_concept'
              'right_route_concept']
}

LOWER_COLUMNS = {
    "offense": ['role', 'alignment', 'player'],
    "defense": ['role', 'alignment', 'player'],
}