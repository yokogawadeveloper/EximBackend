from rest_framework import routers
from master.views import *
from trade.views import *

# Add routers here.
router = routers.DefaultRouter()

# ----------------------------- Master ------------------------------------------- #
router.register('role_master', RoleMasterViewSet, basename='role_master')
router.register('module_master', ModuleMasterViewSet, basename='module_master')
router.register('user_role', UserRoleViewSet, basename='user_role')

# ----------------------------- Trade ------------------------------------------- #
router.register('master_item_batch', MasterItemBatchViewSet, basename='master_item_batch')
router.register('inline_item', InlineItemViewSet, basename='inline_item')
