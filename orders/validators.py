from django import forms


# Валидация правильности ввода ИНН
def validate_len_of_tin(value):
    # Проверка длины ИНН
    if len(value) != 10 and len(value) != 12:
        raise forms.ValidationError(
            'Ваш ИНН должен состоять из 10символов(Юр.лицо) или 12символов(ИП)',
            params={'value': value},
        )


