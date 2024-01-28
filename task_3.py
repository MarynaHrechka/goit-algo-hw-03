import re

def normalize_phone(phone_number: str)-> list:
    pattern = r"\D"
    only_digits =  re.sub(pattern, "", phone_number)
    result = f"+{'' if only_digits.startswith('38') else '38'}{only_digits}"
    return result

