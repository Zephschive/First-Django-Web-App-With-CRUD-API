import logging
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.utils.deprecation import MiddlewareMixin


logger = logging.getLogger(__name__)

class GlobalExceptionHandlerMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, ObjectDoesNotExist):
            logger.error(f"Object not found: {str(exception)}", exc_info=True)
            return JsonResponse({
                "message": "Resource not found",
                "details": str(exception) 
            }, status=404)      
        else:
            logger.error(f"Unhandled exception: {str(exception)}", exc_info=True)
            return JsonResponse({
                "message": "An unexpected error occurred",
                "details": str(exception)
            }, status=500)
