from django.contrib.auth.models import User


def check_superuser():
    if not User.objects.exists():
        user = User.objects.create_user('admin', '', 'admin')
        
        user.is_superuser = 1
        user.is_staff = 1
        user.save()
    else:
        user = User.objects.get(id= 1)
    return user
    