from django.urls import path
from .views import *

urlpatterns = [
    # Pages
    path('', IndexView.as_view(), name='index'),
    path('pages/starter-page', StarterPageView.as_view(), name='starter_page'),
    path('pages/contact-list', ContactListView.as_view(), name='contact_list'),
    path('pages/profile', ProfileView.as_view(), name='profile'),
    path('pages/timeline', TimelineView.as_view(), name='timeline'),
    path('pages/invoice', InvoiceView.as_view(), name='invoice'),
    path('pages/faq', FAQView.as_view(), name='faq'),
    path('pages/pricing', PricingView.as_view(), name='pricing'),
    path('pages/maintenance', MaintenanceView.as_view(), name='maintenance'),
    path('pages/error-404', Error404View.as_view(), name='error_404'),
    path('pages/error-404-alt', Error404AltView.as_view(), name='error_404_alt'),
    path('pages/error-500', Error500View.as_view(), name='error_500'),
    
    # Authentication
    path('authentication/login', LoginView.as_view(), name='login'),
    path('authentication/register', RegisterView.as_view(), name='register'),
    path('authentication/logout', LogoutView.as_view(), name='logout'),
    path('authentication/forgot-password', ForgotPasswordView.as_view(), name='forgot_password'),
    path('authentication/lock-screen', LockScreenView.as_view(), name='lock_screen'),

    # Layouts
    path('layouts/horizontal', HorizontalView.as_view(), name='horizontal'),
    path('layouts/light-sidebar', LightSidebarView.as_view(), name='light_sidebar'),
    path('layouts/small-sidebar', SmallSidebarView.as_view(), name='small_sidebar'),
    path('layouts/collapsed-sidebar', CollapsedSidebarView.as_view(), name='collapsed_sidebar'),
    path('layouts/unsticky-layout', UnstickyLayoutView.as_view(), name='unsticky_layout'),
    path('layouts/boxed-layout', BoxedLayoutView.as_view(), name='boxed_layout'),

    # Basic UI
    path('basic-ui/accordions', AccordionsView.as_view(), name='accordions'),
    path('basic-ui/alerts', AlertsView.as_view(), name='alerts'),
    path('basic-ui/avatars', AvatarsView.as_view(), name='avatars'),
    path('basic-ui/buttons', ButtonsView.as_view(), name='buttons'),
    path('basic-ui/badges', BadgesView.as_view(), name='badges'),
    path('basic-ui/breadcrumb', BreadcrumbView.as_view(), name='breadcrumb'),
    path('basic-ui/cards', CardsView.as_view(), name='cards'),
    path('basic-ui/carousel', CarouselView.as_view(), name='carousel'),
    path('basic-ui/collapse', CollapseView.as_view(), name='collapse'),
    path('basic-ui/dropdowns', DropdownsView.as_view(), name='dropdowns'),
    path('basic-ui/embed-video', EmbedVideoView.as_view(), name='embed_video'),
    path('basic-ui/grid', GridView.as_view(), name='grid'),
    path('basic-ui/links', LinksView.as_view(), name='links'),
    path('basic-ui/list-group', ListGroupView.as_view(), name='list_group'),
    path('basic-ui/modals', ModalsView.as_view(), name='modals'),
    path('basic-ui/notifications', NotificationsView.as_view(), name='notifications'),
    path('basic-ui/offcanvas', OffcanvasView.as_view(), name='offcanvas'),
    path('basic-ui/placeholders', PlaceholdersView.as_view(), name='placeholders'),
    path('basic-ui/pagination', PaginationView.as_view(), name='pagination'),
    path('basic-ui/popovers', PopoversView.as_view(), name='popovers'),
    path('basic-ui/progress', ProgressView.as_view(), name='progress'),
    path('basic-ui/spinners', SpinnersView.as_view(), name='spinners'),
    path('basic-ui/tabs', TabsView.as_view(), name='tabs'),
    path('basic-ui/tooltips', TooltipsView.as_view(), name='tooltips'),
    path('basic-ui/typography', TypographyView.as_view(), name='typography'),
    path('basic-ui/utilities', UtilitiesView.as_view(), name='utilities'),

    # Extended UI
    path('extended-ui/portlets', PortletsView.as_view(), name='portlets'),
    path('extended-ui/scrollbar', ScrollbarView.as_view(), name='scrollbar'),
    path('extended-ui/range-slider', RangeSliderView.as_view(), name='range_slider'),
    path('extended-ui/scrollspy', ScrollspyView.as_view(), name='scrollspy'),

    # Icons
    path('icons/remix-icons', RemixIconsView.as_view(), name='remix_icons'),
    path('icons/bootstrap-icons', BootstrapIconsView.as_view(), name='bootstrap_icons'),
    path('icons/material-design-icons', MaterialDesignIconsView.as_view(), name='material_design_icons'),

    # Charts
    path('charts/apex-charts', ApexChartsView.as_view(), name='apex_charts'),
    path('charts/chartjs', ChartjsView.as_view(), name='chartjs'),
    path('charts/sparkline-charts', SparklineChartsView.as_view(), name='sparkline_charts'),


    # Forms
    path('forms/basic-elements', BasicElementsView.as_view(), name="basic_elements"),
    path('forms/form-advanced', FormAdvancedView.as_view(), name="form_advanced"),
    path('forms/form-validation', FormValidationView.as_view(), name="form_validation"),
    path('forms/form-wizard', FormWizardView.as_view(), name="form_wizard"),
    path('forms/file-uploads', FileUploadsView.as_view(), name="file_uploads"),
    path('forms/form-editors', FormEditorsView.as_view(), name="form_editors"),
    path('forms/image-crop', ImageCropView.as_view(), name="image_crop"),
    path('forms/x-editable', XEditableView.as_view(), name="x_editable"),
    
    # Tables
    path('tables/basic-tables', BasicTablesView.as_view(), name="basic_tables"),
    path('tables/data-tables', DataTablesView.as_view(), name="data_tables"),
    path('tables/editable-tables', EditableTablesView.as_view(), name="editable_tables"),
    path('tables/responsive-table', ResponsiveTableView.as_view(), name="responsive_table"),
    
    # Maps
    path('maps/google-maps', GoogleMapsView.as_view(), name="google_maps"),
    path('maps/vector-maps', VectorMapsView.as_view(), name="vector_maps"),
]
