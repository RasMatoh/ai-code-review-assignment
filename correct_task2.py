def count_valid_emails(emails):
    valid_count = 0

    for email in emails:
        if not isinstance(email, str):
            continue

        parts = email.split('@')
        if len(parts) != 2:
            continue

        local, domain = parts
        if not local or not domain or '.' not in domain:
            continue

        valid_count += 1

    return valid_count