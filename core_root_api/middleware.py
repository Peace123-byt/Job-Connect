import logging
from django.http import JsonResponse
from django.http import HttpResponseForbidden

logger = logging.getLogger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Dictionary to track request counts per IP
        self.ip_request_count = {}

    def __call__(self, request):
        # Get the client's IP address
        ip_address = self.get_client_ip(request)

        # Log the request with IP address
        logger.info(f"Request from IP: {ip_address} - {request.method} {request.path}")

        # Check if the IP has exceeded the request limit
        if self.is_ip_blocked(ip_address):
            logger.warning(f"Blocked IP: {ip_address} - Too many requests")
            return JsonResponse({"message": "Too many requests. You are blocked."}, status=401)

        # Increment the request count for the IP
        self.increment_request_count(ip_address)

        response = self.get_response(request)

        # Log the response status code
        logger.info(f"Response Status Code: {response.status_code}")

        # Log the User-Agent header
        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
        logger.info(f"User-Agent: {user_agent}")

        # Log the response body (if available)
        if hasattr(response, 'content'):
            try:
                response_body = response.content.decode('utf-8')
                logger.info(f"Response Body: {response_body}")
            except UnicodeDecodeError:
                logger.info("Response Body: [Binary or Non-Text Content]")
        else:
            logger.info("Response Body: [No Content]")

        return response

    def get_client_ip(self, request):
        """
        Get the client's IP address from the request.
        Handles cases where the application is behind a proxy or load balancer.
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def increment_request_count(self, ip_address):
        """
        Increment the request count for the given IP address.
        """
        if ip_address in self.ip_request_count:
            self.ip_request_count[ip_address] += 1
        else:
            self.ip_request_count[ip_address] = 1

    def is_ip_blocked(self, ip_address):
        """
        Check if the IP address has exceeded the request limit (3 requests).
        """
        return self.ip_request_count.get(ip_address, 0) >= 3



class ApiKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check for API key in headers
        api_key = request.headers.get('X-API-KEY')
        if api_key != 'MY_SECRET_KEY':
            return HttpResponseForbidden("Invalid API Key")

        response = self.get_response(request)
        return response

from django.http import JsonResponse

class BearerTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get Authorization header
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Missing or invalid Authorization header"}, status=403)

        # Extract the token (removing 'Bearer ' prefix)
        token = auth_header.split("Bearer ")[1]

        # Check if token is valid (replace with your validation logic)
        if token != "MY_SECRET_TOKEN":  # Replace with your actual token validation logic
            return JsonResponse({"error": "Invalid token"}, status=403)

        return self.get_response(request)