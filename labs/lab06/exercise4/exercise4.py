def synchronize_databases(legacy_list, modern_set, blacklist):
    sanitized_legacy_ids = set()

    for record in legacy_list :
        user_id = record[0]
        email = record[1]

        if email not in blacklist : 
            sanitized_legacy_ids.add(user_id)


    lost_id = sanitized_legacy_ids - modern_set

    ghost_id = modern_set - sanitized_legacy_ids

    return lost_id, ghost_id

