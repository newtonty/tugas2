from django.forms import ModelForm
from study_tracker.models import AssignmentRecord

class AssignmentRecordForm(ModelForm):
    class Meta:
        model = AssignmentRecord
        fields = ["name", "subject", "date", "progress", "description"]
