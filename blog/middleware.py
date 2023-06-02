from django.shortcuts import redirect
from django.contrib import admin



class RestrictAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and not request.user.is_superuser:
            return redirect('home')  # Replace 'home' with the URL name of the page you want to redirect non-admin users to
        return self.get_response(request)


# class RestrictAdminMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.path.startswith(admin.site.urls) and not request.user.is_superuser:
#             return redirect('home')  
#         return self.get_response(request)
