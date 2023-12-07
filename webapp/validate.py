def validate(description, status):
    errors = {}
    if not description:
        errors['description'] = 'Обязательное поле'
    elif len(description) > 40:
        errors['description'] = 'Максимальня длина 40'

    if not status:
        errors['status'] = 'Обязательное поле'

    return errors