from authentication.models import Person


def unset_password(backend, user, response, *args, **kwargs):
    print(args)
    person = Person.objects.get(pk=user.id)
    person.password = None
    person.save()
