# chats/middleware.py
import logging
from datetime import datetime

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logging.basicConfig(
            filename='requests.log',
            level=logging.INFO,
            format='%(message)s'
        )

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        logging.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        return self.get_response(request)
  # chats/middleware.py
from django.http import HttpResponseForbidden
from datetime import datetime

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour
        if current_hour < 6 or current_hour > 21:
            return HttpResponseForbidden("Access to chat is restricted during this time.")
        return self.get_response(request)
    # chats/middleware.py
from django.core.cache import cache
from django.http import JsonResponse
import time

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and '/messages' in request.path:
            ip = self.get_client_ip(request)
            current_time = int(time.time())
            window_key = f"{ip}:{current_time // 60}"
            message_count = cache.get(window_key, 0)

            if message_count >= 5:
                return JsonResponse(
                    {"error": "Message limit exceeded. Try again later."},
                    status=429
                )

            cache.set(window_key, message_count + 1, timeout=60)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
  # chats/middleware.py
from django.http import HttpResponseForbidden

class RolePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_paths = ['/admin-action/', '/delete-message/']
        if any(path in request.path for path in restricted_paths):
            if not request.user.is_authenticated or request.user.role not in ['admin', 'moderator']:
                return HttpResponseForbidden("You do not have permission to perform this action.")
        return self.get_response(request)
      
  
