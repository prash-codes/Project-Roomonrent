from django.forms import ModelForm
from ror.models import Feedback, Room


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"