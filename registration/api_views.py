from django.http import JsonResponse
from .models import Student


def student_api(request):
    if not request.user.is_authenticated:
        return JsonResponse(
            {'error': 'Authentication required'},
            status=401
        )

    if request.method != 'GET':
        return JsonResponse(
            {'error': 'Method not allowed'},
            status=405
        )

    students = Student.objects.all()

    data = {
        'count': students.count(),
        'students': [
            {
                'id': student.id,
                'student_name': getattr(student, 'student_name', str(student)),
                'program': getattr(student, 'program', ''),
                'year_level': getattr(student, 'year_level', ''),
                'email': getattr(student, 'email', ''),
            }
            for student in students
        ]
    }

    return JsonResponse(data)