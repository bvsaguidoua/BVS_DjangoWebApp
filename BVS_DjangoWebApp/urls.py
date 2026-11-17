from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # <-- Added this import for settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("registration/", include("registration.urls")),
    path("api/", include("registration.api_urls")),  # Notice it uses include()!
    path("accounts/", include("django.contrib.auth.urls")),
]

# <-- Added this block at the very bottom
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]