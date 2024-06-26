from django.db import models
from django.contrib.auth.models import User

class EmployeeClockIn(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    clock_in_time = models.DateTimeField()
    clock_out_time = models.DateTimeField(null=True, blank=True)
    approved_by_superuser = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_clockins')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee.username} - Clock In: {self.clock_in_time} - Clock Out: {self.clock_out_time}"

    def approve_clock_in(self, superuser):
        if superuser.is_superuser:
            self.approved_by_superuser = True
            self.approved_by = superuser
            self.save()

    def clock_out(self):
        self.clock_out_time = timezone.now()
        self.save()



