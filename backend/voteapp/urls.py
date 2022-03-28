"""voteapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from polls.urls import router as polls_router
from rest_framework.schemas import get_schema_view
from users.urls import router as users_router

urlpatterns = [
    # Django Rest Framework
    path("", include(users_router.urls)),
    path("api/v1/", include(polls_router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
    # Route TemplateView to serve Swagger UI template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    path("openapi", get_schema_view(title="VoteApp API", description="API for VoteApp", version="1.0.0"), name="openapi-schema"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
