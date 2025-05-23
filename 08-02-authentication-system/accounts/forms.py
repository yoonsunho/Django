from django.contrib.auth import get_user_model  # 현재 프로젝트에서 활성화된 사용자 모댈반환
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = User
        model = get_user_model()
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        # model = User
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)