def mask_card_number(user_card_number: str) -> str:
    """
    Функция принимает номер банковской карты и возвращает ее маску.
    """
    masked_number = user_card_number[:4] + " " + user_card_number[4:6] + "** ****" + " " + user_card_number[12:]
    return masked_number


def mask_account_number(user_account_number: str) -> str:
    """
    Функция принимает номер счета и возвращает маску счета.
    """
    masked_number = "**" + user_account_number[-4:]
    return masked_number


def convert_date(input_date):
    date_parts = input_date.split('T')[0].split('-')
    return f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"
