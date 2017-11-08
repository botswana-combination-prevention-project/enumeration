from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_dashboard.view_mixins import ListboardFilterViewMixin
from edc_dashboard.views import ListboardView as BaseListboardView
from edc_navbar import NavbarViewMixin
from household_dashboard.view_mixins import HouseholdQuerysetViewMixin
from plot_dashboard.view_mixins import PlotQuerysetViewMixin
from survey import SurveyViewMixin, SurveyQuerysetViewMixin

from .listboard_filters import HouseholdStructureListboardViewFilters
from ..model_wrappers import HouseholdStructureWithLogEntryWrapper


class ListboardView(AppConfigViewMixin, NavbarViewMixin, EdcBaseViewMixin,
                    ListboardFilterViewMixin,
                    HouseholdQuerysetViewMixin, PlotQuerysetViewMixin,
                    SurveyViewMixin, SurveyQuerysetViewMixin, BaseListboardView):

    app_config_name = 'enumeration'

    navbar_name = settings.MAIN_NAVBAR_NAME
    navbar_selected_item = 'enumeration'

    model = 'household.householdstructure'
    model_wrapper_cls = HouseholdStructureWithLogEntryWrapper
    paginate_by = 10
    plot_queryset_lookups = ['household', 'plot']
    household_queryset_lookups = ['household']
    listboard_view_filters = HouseholdStructureListboardViewFilters()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
