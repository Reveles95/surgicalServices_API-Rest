from rest_framework import routers
from .viewset import *

router = routers.SimpleRouter()
router.register('', ServicesViewset)
router.register('api/v1.0/specialistsTeam', specialistsTeamViewset)

urlpatterns = router.urls