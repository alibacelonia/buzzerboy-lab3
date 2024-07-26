from django.shortcuts import render
from django.http import HttpResponse
from .sidebar_items import sidebar_items
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'pages/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Index"
        context['segment'] = ['dashboard']
        context['sidebar_items'] = sidebar_items
        return context
    
# --------------------------------------------------------------------------------------------------------------------------------
    # Pages 
# --------------------------------------------------------------------------------------------------------------------------------
class StarterPageView(TemplateView):
    template_name = 'pages/starter_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Starter Page"
        context['segment'] = ['pages', 'starter_page']
        context['sidebar_items'] = sidebar_items
        return context
    
class ContactListView(TemplateView):
    template_name = 'pages/contact_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Contact List"
        context['segment'] = ['pages', 'contact_list']
        context['sidebar_items'] = sidebar_items
        return context

class ProfileView(TemplateView):
    template_name = 'pages/profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Profile"
        context['segment'] = ['pages', 'profile']
        context['sidebar_items'] = sidebar_items
        return context

class TimelineView(TemplateView):
    template_name = 'pages/timeline.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Timeline"
        context['segment'] = ['pages', 'timeline']
        context['sidebar_items'] = sidebar_items
        return context

class InvoiceView(TemplateView):
    template_name = 'pages/invoice.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Invoice"
        context['segment'] = ['pages', 'invoice']
        context['sidebar_items'] = sidebar_items
        return context

class FAQView(TemplateView):
    template_name = 'pages/faq.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "FAQ"
        context['segment'] = ['pages', 'faq']
        context['sidebar_items'] = sidebar_items
        return context

class PricingView(TemplateView):
    template_name = 'pages/pricing.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Pricing"
        context['segment'] = ['pages', 'pricing']
        context['sidebar_items'] = sidebar_items
        return context

class MaintenanceView(TemplateView):
    template_name = 'pages/maintenance.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Maintenance"
        context['segment'] = ['pages', 'maintenance']
        context['sidebar_items'] = sidebar_items
        return context

class Error404View(TemplateView):
    template_name = 'pages/error_404.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Error 404"
        context['segment'] = ['pages', 'error_404']
        context['sidebar_items'] = sidebar_items
        return context

class Error404AltView(TemplateView):
    template_name = 'pages/error_404_alt.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Error 404-alt"
        context['segment'] = ['pages', 'error_404_alt']
        context['sidebar_items'] = sidebar_items
        return context

class Error500View(TemplateView):
    template_name = 'pages/error_500.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Error 500"
        context['segment'] = ['pages', 'error_500']
        context['sidebar_items'] = sidebar_items
        return context

# --------------------------------------------------------------------------------------------------------------------------------
    # Authentication 
# --------------------------------------------------------------------------------------------------------------------------------
class LoginView(TemplateView):
    template_name = 'authentication/login.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Login"
        context['segment'] = ['authentication', 'login']
        context['sidebar_items'] = sidebar_items
        return context

class RegisterView(TemplateView):
    template_name = 'authentication/register.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Register"
        context['segment'] = ['authentication', 'register']
        context['sidebar_items'] = sidebar_items
        return context

class LogoutView(TemplateView):
    template_name = 'authentication/logout.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Logout"
        context['segment'] = ['authentication', 'logout']
        context['sidebar_items'] = sidebar_items
        return context

class ForgotPasswordView(TemplateView):
    template_name = 'authentication/forgot_password.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Forgot Password"
        context['segment'] = ['authentication', 'forgot_password']
        context['sidebar_items'] = sidebar_items
        return context

class LockScreenView(TemplateView):
    template_name = 'authentication/lock_screen.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Lock Screen"
        context['segment'] = ['authentication', 'lock_screen']
        context['sidebar_items'] = sidebar_items
        return context

# --------------------------------------------------------------------------------------------------------------------------------
    # Layouts 
# --------------------------------------------------------------------------------------------------------------------------------
class HorizontalView(TemplateView):
    template_name = 'layouts/horizontal.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Horizontal"
        context['segment'] = ['layouts', 'horizontal']
        context['sidebar_items'] = sidebar_items
        return context

class LightSidebarView(TemplateView):
    template_name = 'layouts/light_sidebar.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Light Sidebar"
        context['segment'] = ['layouts', 'light_sidebar']
        context['sidebar_items'] = sidebar_items
        return context

class SmallSidebarView(TemplateView):
    template_name = 'layouts/small_sidebar.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Small Sidebar"
        context['segment'] = ['layouts', 'small_sidebar']
        context['sidebar_items'] = sidebar_items
        return context

class CollapsedSidebarView(TemplateView):
    template_name = 'layouts/collapsed_sidebar.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Collapsed Sidebar"
        context['segment'] = ['layouts', 'collapsed_sidebar']
        context['sidebar_items'] = sidebar_items
        return context

class UnstickyLayoutView(TemplateView):
    template_name = 'layouts/unsticky_layout.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Unsticky Layout"
        context['segment'] = ['layouts', 'unsticky_layout']
        context['sidebar_items'] = sidebar_items
        return context

class BoxedLayoutView(TemplateView):
    template_name = 'layouts/boxed_layout.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Boxed Layout"
        context['segment'] = ['layouts', 'boxed_layout']
        context['sidebar_items'] = sidebar_items
        return context

# --------------------------------------------------------------------------------------------------------------------------------
    # Basic UI 
# --------------------------------------------------------------------------------------------------------------------------------
class AccordionsView(TemplateView):
    template_name = 'basic_ui/accordions.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Accordions"
        context['segment'] = ['basic_ui', 'accordions']
        context['sidebar_items'] = sidebar_items
        return context

class AlertsView(TemplateView):
    template_name = 'basic_ui/alerts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Alerts"
        context['segment'] = ['basic_ui', 'alerts']
        context['sidebar_items'] = sidebar_items
        return context

class AvatarsView(TemplateView):
    template_name = 'basic_ui/avatars.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Avatars"
        context['segment'] = ['basic_ui', 'avatars']
        context['sidebar_items'] = sidebar_items
        return context

class ButtonsView(TemplateView):
    template_name = 'basic_ui/buttons.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Buttons"
        context['segment'] = ['basic_ui', 'buttons']
        context['sidebar_items'] = sidebar_items
        return context

class BadgesView(TemplateView):
    template_name = 'basic_ui/badges.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Badges"
        context['segment'] = ['basic_ui', 'badges']
        context['sidebar_items'] = sidebar_items
        return context

class BreadcrumbView(TemplateView):
    template_name = 'basic_ui/breadcrumb.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Breadcrumb"
        context['segment'] = ['basic_ui', 'breadcrumb']
        context['sidebar_items'] = sidebar_items
        return context

class CardsView(TemplateView):
    template_name = 'basic_ui/cards.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Cards"
        context['segment'] = ['basic_ui', 'cards']
        context['sidebar_items'] = sidebar_items
        return context

class CarouselView(TemplateView):
    template_name = 'basic_ui/carousel.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Carousel"
        context['segment'] = ['basic_ui', 'carousel']
        context['sidebar_items'] = sidebar_items
        return context

class CollapseView(TemplateView):
    template_name = 'basic_ui/collapse.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Collapse"
        context['segment'] = ['basic_ui', 'collapse']
        context['sidebar_items'] = sidebar_items
        return context

class DropdownsView(TemplateView):
    template_name = 'basic_ui/dropdowns.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Dropdowns"
        context['segment'] = ['basic_ui', 'dropdowns']
        context['sidebar_items'] = sidebar_items
        return context

class EmbedVideoView(TemplateView):
    template_name = 'basic_ui/embed_video.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Embed Video"
        context['segment'] = ['basic_ui', 'embed_video']
        context['sidebar_items'] = sidebar_items
        return context

class GridView(TemplateView):
    template_name = 'basic_ui/grid.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Grid"
        context['segment'] = ['basic_ui', 'grid']
        context['sidebar_items'] = sidebar_items
        return context

class LinksView(TemplateView):
    template_name = 'basic_ui/links.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Links"
        context['segment'] = ['basic_ui', 'links']
        context['sidebar_items'] = sidebar_items
        return context

class ListGroupView(TemplateView):
    template_name = 'basic_ui/list_group.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "List Group"
        context['segment'] = ['basic_ui', 'list_group']
        context['sidebar_items'] = sidebar_items
        return context

class ModalsView(TemplateView):
    template_name = 'basic_ui/modals.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Modals"
        context['segment'] = ['basic_ui', 'modals']
        context['sidebar_items'] = sidebar_items
        return context

class NotificationsView(TemplateView):
    template_name = 'basic_ui/notifications.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Notifications"
        context['segment'] = ['basic_ui', 'notifications']
        context['sidebar_items'] = sidebar_items
        return context

class OffcanvasView(TemplateView):
    template_name = 'basic_ui/offcanvas.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Offcanvas"
        context['segment'] = ['basic_ui', 'offcanvas']
        context['sidebar_items'] = sidebar_items
        return context

class PlaceholdersView(TemplateView):
    template_name = 'basic_ui/placeholders.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Placeholders"
        context['segment'] = ['basic_ui', 'placeholders']
        context['sidebar_items'] = sidebar_items
        return context

class PaginationView(TemplateView):
    template_name = 'basic_ui/pagination.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Pagination"
        context['segment'] = ['basic_ui', 'pagination']
        context['sidebar_items'] = sidebar_items
        return context

class PopoversView(TemplateView):
    template_name = 'basic_ui/popovers.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Popovers"
        context['segment'] = ['basic_ui', 'popovers']
        context['sidebar_items'] = sidebar_items
        return context

class ProgressView(TemplateView):
    template_name = 'basic_ui/progress.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Progress"
        context['segment'] = ['basic_ui', 'progress']
        context['sidebar_items'] = sidebar_items
        return context

class SpinnersView(TemplateView):
    template_name = 'basic_ui/spinners.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Spinners"
        context['segment'] = ['basic_ui', 'spinners']
        context['sidebar_items'] = sidebar_items
        return context

class TabsView(TemplateView):
    template_name = 'basic_ui/tabs.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Tabs"
        context['segment'] = ['basic_ui', 'tabs']
        context['sidebar_items'] = sidebar_items
        return context

class TooltipsView(TemplateView):
    template_name = 'basic_ui/tooltips.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Tooltips"
        context['segment'] = ['basic_ui', 'tooltips']
        context['sidebar_items'] = sidebar_items
        return context

class TypographyView(TemplateView):
    template_name = 'basic_ui/typography.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Typography"
        context['segment'] = ['basic_ui', 'typography']
        context['sidebar_items'] = sidebar_items
        return context

class UtilitiesView(TemplateView):
    template_name = 'basic_ui/utilities.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Utilities"
        context['segment'] = ['basic_ui', 'utilities']
        context['sidebar_items'] = sidebar_items
        return context

# --------------------------------------------------------------------------------------------------------------------------------
    # Extended UI 
# --------------------------------------------------------------------------------------------------------------------------------
class PortletsView(TemplateView):
    template_name = 'extended_ui/portlets.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Portlets"
        context['segment'] = ['extended_ui', 'portlets']
        context['sidebar_items'] = sidebar_items
        return context

class ScrollbarView(TemplateView):
    template_name = 'extended_ui/scrollbar.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Scrollbar"
        context['segment'] = ['extended_ui', 'scrollbar']
        context['sidebar_items'] = sidebar_items
        return context

class RangeSliderView(TemplateView):
    template_name = 'extended_ui/range_slider.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Range Slider"
        context['segment'] = ['extended_ui', 'range_slider']
        context['sidebar_items'] = sidebar_items
        return context

class ScrollspyView(TemplateView):
    template_name = 'extended_ui/scrollspy.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Scrollspy"
        context['segment'] = ['extended_ui', 'scrollspy']
        context['sidebar_items'] = sidebar_items
        return context

# --------------------------------------------------------------------------------------------------------------------------------
    # Icons 
# --------------------------------------------------------------------------------------------------------------------------------
class RemixIconsView(TemplateView):
    template_name = 'icons/remix_icons.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Remix Icons"
        context['segment'] = ['icons', 'remix_icons']
        context['sidebar_items'] = sidebar_items
        return context

class BootstrapIconsView(TemplateView):
    template_name = 'icons/bootstrap_icons.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Bootstrap Icons"
        context['segment'] = ['icons', 'bootstrap_icons']
        context['sidebar_items'] = sidebar_items
        return context

class MaterialDesignIconsView(TemplateView):
    template_name = 'icons/material_design_icons.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Material Design Icons"
        context['segment'] = ['icons', 'material_design_icons']
        context['sidebar_items'] = sidebar_items
        return context

# --------------------------------------------------------------------------------------------------------------------------------
    # Charts 
# --------------------------------------------------------------------------------------------------------------------------------
class ApexChartsView(TemplateView):
    template_name = 'charts/apex_charts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Apex Charts"
        context['segment'] = ['charts', 'apex_charts']
        context['sidebar_items'] = sidebar_items
        return context

class ChartjsView(TemplateView):
    template_name = 'charts/chartjs.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Chart.js"
        context['segment'] = ['charts', 'chartjs']
        context['sidebar_items'] = sidebar_items
        return context

class SparklineChartsView(TemplateView):
    template_name = 'charts/sparkline_charts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Sparkline Charts"
        context['segment'] = ['charts', 'sparkline_charts']
        context['sidebar_items'] = sidebar_items
        return context

# --------------------------------------------------------------------------------------------------------------------------------
    # Forms 
# --------------------------------------------------------------------------------------------------------------------------------

class BasicElementsView(TemplateView):
    template_name = 'forms/basic_elements.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Basic Elements"
        context['segment'] = ['forms', 'basic_elements']
        context['sidebar_items'] = sidebar_items
        return context
    
class FormAdvancedView(TemplateView):
    template_name = 'forms/form_advanced.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Form Advanced"
        context['segment'] = ['forms', 'form_advanced']
        context['sidebar_items'] = sidebar_items
        return context
    
class FormValidationView(TemplateView):
    template_name = 'forms/form_validation.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Form Validation"
        context['segment'] = ['forms', 'form_validation']
        context['sidebar_items'] = sidebar_items
        return context
    
class FormWizardView(TemplateView):
    template_name = 'forms/form_wizard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Form Wizard"
        context['segment'] = ['forms', 'form_wizard']
        context['sidebar_items'] = sidebar_items
        return context
    
class FileUploadsView(TemplateView):
    template_name = 'forms/file_uploads.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Form Uploads"
        context['segment'] = ['forms', 'file_uploads']
        context['sidebar_items'] = sidebar_items
        return context
    
class FormEditorsView(TemplateView):
    template_name = 'forms/form_editors.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Form Editors"
        context['segment'] = ['forms', 'form_editors']
        context['sidebar_items'] = sidebar_items
        return context
    
class ImageCropView(TemplateView):
    template_name = 'forms/image_crop.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Image Crop"
        context['segment'] = ['forms', 'image_crop']
        context['sidebar_items'] = sidebar_items
        return context
    
class XEditableView(TemplateView):
    template_name = 'forms/x_editable.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "X Editable"
        context['segment'] = ['forms', 'x_editable']
        context['sidebar_items'] = sidebar_items
        return context
    
# --------------------------------------------------------------------------------------------------------------------------------
    # Tables 
# --------------------------------------------------------------------------------------------------------------------------------

class BasicTablesView(TemplateView):
    template_name = 'tables/basic_tables.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Basic Tables"
        context['segment'] = ['tables', 'basic_tables']
        context['sidebar_items'] = sidebar_items
        return context
    
class DataTablesView(TemplateView):
    template_name = 'tables/data_tables.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Data Tables"
        context['segment'] = ['tables', 'data_tables']
        context['sidebar_items'] = sidebar_items
        return context
    
class EditableTablesView(TemplateView):
    template_name = 'tables/editable_tables.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Editable Tables"
        context['segment'] = ['tables', 'editable_tables']
        context['sidebar_items'] = sidebar_items
        return context
    
class ResponsiveTableView(TemplateView):
    template_name = 'tables/responsive_table.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Responsive Table"
        context['segment'] = ['tables', 'responsive_table']
        context['sidebar_items'] = sidebar_items
        return context
    
# --------------------------------------------------------------------------------------------------------------------------------
    # Maps 
# --------------------------------------------------------------------------------------------------------------------------------

class GoogleMapsView(TemplateView):
    template_name = 'maps/google_maps.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Google Maps"
        context['segment'] = ['maps', 'google_maps']
        context['sidebar_items'] = sidebar_items
        return context
    
class VectorMapsView(TemplateView):
    template_name = 'maps/vector_maps.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Vector Maps"
        context['segment'] = ['maps', 'google_maps']
        context['sidebar_items'] = sidebar_items
        return context