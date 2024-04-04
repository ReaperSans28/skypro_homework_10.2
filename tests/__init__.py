from src.masks import mask_account_number, mask_card_number

user_input = input()

if "Счет" in user_input:
    print(f"Счет {mask_account_number(user_input)}")
else:
    print(f"{mask_card_number(user_input)}")
