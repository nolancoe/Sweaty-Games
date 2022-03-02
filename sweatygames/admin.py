from django.contrib import admin
from .models import Match
from .models import user_profile
from .models import Season
from .models import Team

admin.site.register(user_profile)
admin.site.register(Match)
admin.site.register(Season)
admin.site.register(Team)




